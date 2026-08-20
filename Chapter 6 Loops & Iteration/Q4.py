# Q4 — break and continue
# Part 1: Write a for loop over a list of server statuses: ["running", "running", "stopped", "running"]. 
# Use break to stop the loop immediately and print "Found a stopped server, stopping check" the moment you hit "stopped".

for server_stat in ["running", "running", "stopped", "running"]:
    if server_stat == "stopped" :
        print("Found a stopped server, stopping check" )
        break
for status in ["running", "running", "stopped", "running"]:
    if status == "running":
        continue
    print("Alert:" , status)
 
        