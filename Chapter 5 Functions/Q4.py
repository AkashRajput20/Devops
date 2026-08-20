# Q4 — Function combining what you've learned (conditionals inside a function)
# Write a function called get_status(disk_usage) that returns the string "Critical" if disk_usage > 90, "Warning"
# if disk_usage > 75, otherwise "Healthy". Call it with a few different values to confirm all three branches work.

def get_status(disk_usage):
    if disk_usage > 90:
        return "Critical"
    elif disk_usage > 75:
        return "Warning"
    else:
        return "Healthy"

statusd1=get_status(99)    
print(statusd1)
    





        
    