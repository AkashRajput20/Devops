# Q2 — Searching for lines
# Open sample_log.txt and print only the lines that contain the word "ERROR".
# Expected output is two lines, the disk usage one and the connection timeout one.

logbox = open ("sample_log.txt")
for issue in logbox:
    issue = issue.rstrip()
    if "ERROR" in issue:
        print(issue)