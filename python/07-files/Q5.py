# Q5 — Mini scenario: writing a simple report

# Read through sample_log.txt, count the total number of INFO lines and ERROR lines separately, and print a summary:

# Log Summary:
# INFO messages: 3
# ERROR messages: 2

aws07 = open("sample_log.txt")
info_count= 0
error_count= 0
for summary in aws07:
    if "ERROR" in summary:
        error_count = error_count + 1
    elif "INFO" in summary:
        info_count = info_count + 1
print("ERROR messages:", error_count)        
print("INFO messages:",info_count)

