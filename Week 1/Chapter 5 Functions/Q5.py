# Q5 — Mini scenario (realistic DevOps utility function)
# Write a function called server_health_check(server_name, cpu, disk, memory) 
# that uses the same Critical/Warning/Healthy logic from your earlier conditional exercise (using or across all three metrics), 
# but this time wrap it in a function that returns a formatted string like "Server web01 status: Critical" instead of just printing
# raw values. Call the function with two or three different servers (different values) 
# to prove it's reusable — this is the real point of functions: write the logic once, reuse it for every server 
# instead of copy-pasting the same check repeatedly.

def server_health_check(server_name, cpu, disk, memory):
    if   cpu > 90 or disk > 90 or memory > 90:
        message1=f"Server {server_name} status: Critical"
        return message1
    elif cpu > 75 or disk > 75 or memory > 75:
         message2=f"Server {server_name} status: Warning"
         return message2
    else:
        message3=f"Server {server_name} status: Healthy"
        return message3

serverhealth=server_health_check("Web01", 79, 79, 78)
print(serverhealth)
    
