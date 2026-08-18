# Q3 — Nested decisions
# Write a script with server_status = "running" and disk_usage = 95. First check if server_status == "running".
#  If it is, do a nested check: if disk_usage > 90, print "Server running but disk critical", else print "Server running, 
# all normal". 
# If server isn't running, print "Server down — check immediately".

server_status="stopped"
disk_usage=95
print(type(disk_usage))
if server_status=="runninng":
    if disk_usage > 90:
       print("Server running but disk critical")

    else:
        print("Server running,all normal")
else: 
        print("Server down — check immediately")

    