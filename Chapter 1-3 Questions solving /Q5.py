# Q5 — Mini scenario (ties directly into your Week 5 capstone project)
# Write a script that:
# Creates server_name (a string, any name you like)
# Creates disk_usage_percent (a number, e.g. 95)
# Creates threshold (a number, e.g. 90)
# Uses a comparison to check if disk_usage_percent is greater than threshold — 
# store the result in a variable called is_critical
# Prints an f-string like: "Server X status: Critical = True" (or False, depending on the values)

server_name=" Raspberry Pi"
print(type(server_name))
disk_usage_percent=75
print(type(disk_usage_percent))
threshold=80
print(type(threshold))
is_critical=disk_usage_percent > threshold
print(type(is_critical))
print(is_critical)
print(f"Server {server_name} status: Critical = {is_critical}")