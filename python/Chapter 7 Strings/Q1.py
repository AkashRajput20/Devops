# Q1 — String indexing and slicing
# You have a log line: log_line = "2026-08-20 ERROR Disk usage exceeded threshold". 
# Use slicing to extract just the date ("2026-08-20") and print it. Then use indexing
# to print just the very first character of the whole string.

log_line = "2026-08-20 ERROR Disk usage exceeded threshold"
print(log_line[0:10])
print(log_line[0:1])