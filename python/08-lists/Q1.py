# Q1 — Read into a list, then loop it twice
# Read sample_log.txt into a list of stripped lines. Then loop over that
# list twice: first print every line, then print how many lines there are.
# Also try looping the file handle twice instead of the list, and see what
# the second loop gives you.

web01_logs = open("sample_log.txt")
web01_alist = web01_logs
for w in web01_logs:
    print(w.rstrip())
for lines in web01_logs:
    print("second pass", lines.rstrip())



 
