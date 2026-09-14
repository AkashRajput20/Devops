# Q3 — Counting matches

# Open sample_log.txt, count how many lines contain "ERROR", and print a final message like Total errors found: 2.

awss1 = open ("sample_log.txt")
error_count = 0
for issue in awss1:
    if "ERROR" in issue:
        error_count = error_count + 1
print("Total errors found:", error_count)