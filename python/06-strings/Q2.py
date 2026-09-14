# Q2 — Searching in strings (realistic log-checking scenario)

# You have log_line = "2026-08-20 ERROR Disk usage exceeded threshold". 
# Use the in keyword to check if the word "ERROR" appears in the line, and print "Alert: error found in log" if it does,
# otherwise print "No errors found".

log_line="2026-08-20 ERROR Disk usage exceeded threshold"
if "ERROR" in log_line:
        print("Alert: error found in log")
else:
        print("No errors found")

# if "Disk" in log_line:
#     print("Alert: error found in log")
# else:
#         print("No errors found")
               