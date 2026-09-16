# Bandit notes

OverTheWire wargame — Linux command line practice.

Connect: `ssh banditN@bandit.labs.overthewire.org -p 2220`

---

## Level 0 — Getting in

Log in and look around.

```bash
ls
cat readme
```

Password: `6y2kwnwK6grgvwvpvLaa2T1cpFEKOhNR`

---

## Level 0 → 1 — Plain file

Password sits in `readme` in the home directory. No trick.

---

## Level 1 → 2 — File named `-`

A leading dash is parsed as an option flag, not a filename. `cat -` tells cat
to read from stdin, so it appears to hang rather than erroring.

```bash
cat ./-
```

Alternatives:
- `cat < -` — redirection resolves the file before cat sees the argument
- `cat -- -` — `--` means "no more options after this point"

Real-world: create a file called `-rf` by accident and you hit this immediately.

Password: `PK8fYLZg2hnHSz83plBL1iEPKdD3QToB`

---

## Level 2 → 3 — Spaces in filename

File is `--spaces in this filename--`. The shell splits arguments on
whitespace, so cat receives four separate arguments instead of one.

```bash
cat "--spaces in this filename--"     # quotes — cleanest
cat --spaces\ in\ this\ filename--    # backslash escaping
```

Tab completion escapes the name automatically. This is the same reason folder
names with spaces cause constant friction.

Password: `7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME`

---

## Level 3 → 4 — Hidden file

`...Hiding-From-You` inside `inhere/`. A leading dot hides a file from `ls`.
Convention, not security.

```bash
ls -la inhere/
cat inhere/...Hiding-From-You
```

- `-a` — show all, including dotfiles
- `-l` — long format: permissions, owner, size, date

`ls -la` is the everyday default. This is why `.gitignore`, `.env` and `.ssh`
stay out of sight — and why people commit secrets in `.env` without noticing.

Password: `xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq`

---

## Level 4 → 5 — Which file is readable

Ten files in `inhere/`, only one is human-readable. Don't `cat` them one by
one: binary output contains escape sequences that garble the terminal.

```bash
file ./*
cat ./-file07
```

`file` identifies type by inspecting the content's magic bytes, not by
extension. Extensions lie; a file called `backup.txt` might be a gzip archive.

Terminal recovery after catting a binary:
- `reset` — reinitialises the terminal properly
- `stty sane` — restores sane input settings
- `clear` / Ctrl+L — only scrolls the screen, does NOT fix broken state

Password: `6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG`

---

## Level 5 → 6 — find with multiple conditions

Many files across 20 directories. Three properties: human-readable,
1033 bytes, not executable.

```bash
find . -type f -size 1033c ! -executable
```

- `-type f` — regular files only, not directories
- `-size 1033c` — the `c` suffix means bytes. Without it, the number means
  512-byte blocks, which is the default and catches everyone once.
- `! -executable` — `!` negates any find condition

Run a command on each result:

```bash
find . -type f -size 1033c ! -executable -exec cat {} \;
```

`{}` is the placeholder for each filename. This pattern comes up constantly —
find all logs older than 30 days and delete them, find all `.tf` files and
format them.

Password: `pXa26xhMWaC2SvDotA4r9EgZkulOeSBW`

---

## Level 6 → 7 — Searching the whole filesystem

"Somewhere on the server" means start from the root, not the current
directory. Conditions: owned by user bandit7, group bandit6, 33 bytes.

```bash
find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
cat /var/lib/dpkg/info/bandit7.password
```

**The important part: `2>/dev/null`**

Two output streams exist and both print to the terminal by default:
- stdout — stream 1 — normal output
- stderr — stream 2 — errors

Searching `/` as an unprivileged user produces hundreds of "Permission denied"
lines that bury the real result. `2>` redirects stream 2 only. `/dev/null`
discards everything written to it.

Related: `2>&1` merges stderr into stdout, useful when piping both together.

Also learnt on a detour: `/etc/passwd` maps usernames to UIDs, one line per
user. `find -user` accepts the name directly, so the lookup isn't needed here.

The password was hidden in `/var/lib/dpkg/info/` — a legitimate package
manager directory. Plausible location, wrong owner. That mismatch between
"looks normal" and "owned by the wrong user" is what real investigation
looks for.

Password: `Bmnnvf82KzQlfxgAI2d1zYbr1u9pr3E3`

---

## Level 7 → 8 — grep

One file, a million lines, find the line containing `millionth`.

```bash
grep millionth data.txt
```

Same job as this Python, in one line:

```python
for line in file:
    if "millionth" in line:
        print(line)
```

Knowing when a shell one-liner beats a script is half of DevOps work.

Password: `VR1ljMayciFxbnUokuQmJFw6QC9VKtub`

---

## Level 8 → 9 — TODO

File with repeated lines, find the one occurring only once.
`sort` and `uniq` are the tools.

---

# Command reference

## Listing
| Command | What it does |
|---|---|
| `ls -la` | Long listing with hidden files. The everyday default. |
| `ls -lah` | Adds human-readable sizes (4.0K, 1.2G). |
| `ls -laht` | Sorts by modification time, newest first. Useful when troubleshooting. |

## Reading
| Command | What it does |
|---|---|
| `cat file` | Print a file. Never use on large files. |
| `cat ./file` | `./` forces the name to be read as a path, not an option. |
| `file ./*` | Identify file types by content. |
| `less file` | Page through a large file. Arrows to scroll, `q` to quit. |
| `head -20` / `tail -20` | First or last 20 lines. |
| `tail -f` | Follow a file live as it grows. Most-used command in real troubleshooting. |

## Finding files
| Command | What it does |
|---|---|
| `find / -name x` | Search the whole filesystem by name. |
| `find . -type f` | Regular files only. |
| `find . -size 33c` | Exact size in bytes (`c` suffix). |
| `find . -user u -group g` | Filter by ownership. |
| `find . ! -executable` | `!` negates any condition. |
| `find . -exec cmd {} \;` | Run a command on each result. |

## Searching inside files
| Command | What it does |
|---|---|
| `grep pattern file` | Print lines containing the pattern. |
| `grep -i` | Case-insensitive. Fixes the `"Error"` vs `"ERROR"` problem. |
| `grep -v` | Invert — print lines NOT matching. |
| `grep -n` | Show line numbers. |
| `grep -c` | Count matches instead of printing. |
| `grep -r` | Recursive, search a directory tree. |
| `grep -A 5` / `-B 5` / `-C 5` | Show lines After / Before / Context around each match. |
| `grep -E "a\|b"` | Extended regex, alternation. |
| `cmd \| grep x` | Filter another command's output. The most common usage. |

## Streams and redirection
| Syntax | What it does |
|---|---|
| `>` | Redirect stdout to a file. Overwrites, no warning. |
| `>>` | Redirect stdout, appending. |
| `2>` | Redirect stderr only. |
| `2>/dev/null` | Discard errors, keep results. |
| `2>&1` | Merge stderr into stdout. |
| `\|` | Pipe one command's output into the next. |

## Terminal
| Command | What it does |
|---|---|
| `reset` | Reinitialise a broken terminal. |
| `stty sane` | Restore sane input settings. |
| `clear` / Ctrl+L | Clear the screen only. |
| `man cmd` | Full reference. Dense. |
| `cmd --help` | Shorter, usually more readable. |
| `tldr cmd` | Practical examples. `sudo apt install tldr` |

---

# Concepts

**Option vs filename.** A leading `-` is parsed as an option. `./` or `--`
disambiguates.

**Argument splitting.** The shell splits on whitespace. Quote or escape names
containing spaces.

**Hidden files.** A leading `.` hides a file from `ls`. Convention only.

**Extensions are not authoritative.** `file` reads the actual content.

**Absolute vs relative paths.** A path starting with `/` works from anywhere.
A bare name resolves from the current directory — the same reason Python's
`open("sample_log.txt")` fails when run from the wrong folder.

**Two output streams.** stdout (1) and stderr (2) are separate and can be
redirected independently.

**Unix philosophy.** Each tool does one thing. The pipe composes them.
Knowing five tools well beats knowing twenty superficially.

Example — count error types by frequency:

```bash
grep ERROR app.log | cut -d' ' -f4 | sort | uniq -c | sort -rn
```

That's the license audit script as a one-liner.

**You are not meant to memorise flags.** Know which tool solves the problem
and that `man` or `--help` will give you the flag. That is the actual skill.