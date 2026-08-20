# Q5 — Mini scenario (functions + loops combined)

# Using your get_status(disk_usage) function from the Functions chapter (the one returning "Critical", "Warning", or "Healthy"), 
# write a for loop that goes through this list of disk usage values: [45, 92, 78, 60, 95], calls get_status() on each one, 
# and prints something like:

def get_status(disk_usage):
    if disk_usage > 90 :
        return "Critical"
    elif disk_usage > 75:
        return "Warning"
    else:
        return "Healthy"

    
for final_disk_status in [45, 92, 78, 60, 95]:
        status = get_status(final_disk_status)
        print(f"Disk usage {final_disk_status}% -> {status}:")
    
    