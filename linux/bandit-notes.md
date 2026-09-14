# Bandit notes

OverTheWire wargame. SSH: `ssh banditN@bandit.labs.overthewire.org -p 2220`

---

## Level 0
Log in and look around.

```bash
ls
cat readme
```

Password: `6y2kwnwK6grgvwvpvLaa2T1cpFEKOhNR`

---

## Level 0 → 1
File is named `readme` in the home directory. Nothing tricky.

---

## Level 1 → 2
File is named `-`. A leading dash is read as an option flag, not a filename.
`cat -` reads from stdin instead and appears to hang.

```bash
cat ./-
```

Other ways: `cat < -` (redirection resolves the file before cat sees it),
`cat -- -` (`--` means no more options).

Password: `PK8fYLZg2hnHSz83plBL1iEPKdD3QToB`

---

## Level 2 → 3
File is `--spaces in this filename--`. The shell splits on whitespace, so cat
receives four arguments instead of one.

```bash
cat "--spaces in this filename--"
cat --spaces\ in\ this\ filename--
```

Quotes are cleaner. Tab completion escapes the name automatically.

Password: `7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME`

---

## Level 3 → 4
File is `...Hiding-From-You` inside `inhere/`. Leading dot means hidden,
so plain `ls` skips it.

```bash
ls -la inhere/
cat inhere/...Hiding-From-You
```

`-a` shows dotfiles, `-l` gives permissions and sizes. `ls -la` is the
everyday default. This is why `.gitignore` and `.env` stay out of sight.

Password: `xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq`

---

## Level 4 → 5
Ten files in `inhere/`, only one is human-readable. Don't cat them one by
one — binary output garbles the terminal.

```bash
file ./*
cat ./-file07
```

`file` identifies type by inspecting content, not by extension. Extensions
lie; magic bytes don't.

If the terminal breaks after catting a binary: `reset`, or `stty sane`.
`clear` only scrolls, it doesn't fix terminal state.

Password: `6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG`

---

## Level 5 → 6
TODO. Many files across many directories. Three conditions: human-readable,
specific size, not executable. `find` has a flag for each.

---

# Commands learned

| Command | What it does |
|---|---|
| `ls -la` | Long listing including hidden files. Everyday default. |
| `ls -lah` | Adds human-readable sizes. |
| `ls -laht` | Sorts by modification time, newest first. Useful when troubleshooting. |
| `cat ./file` | `./` forces a name to be read as a path, not an option. |
| `cat < file` | Redirection. Shell opens the file, cat reads stdin. |
| `file ./*` | Identifies file types by content. |
| `find` | Searches a directory tree. Takes conditions. |
| `reset` | Reinitialises a broken terminal. |
| `clear` / Ctrl+L | Clears the screen only. |

# Concepts

- A leading `-` is parsed as an option. `./` or `--` disambiguates.
- The shell splits arguments on whitespace. Quote or escape names with spaces.
- A leading `.` hides a file from `ls`. Convention, not security.
- File extensions are not authoritative. `file` reads the actual content.