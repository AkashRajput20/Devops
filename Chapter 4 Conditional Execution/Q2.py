# Q2 — elif (multi-way decision)
# Write a script with cpu_usage = 65. Use if/elif/else to print:

# "Critical" if cpu_usage > 90
# "Warning" if cpu_usage > 70
# "Normal" otherwise

cpu_usage=65
if cpu_usage > 90 :
     print("Critical")

elif cpu_usage > 70 : 
    print("Warning")

else :
    print("Normal")