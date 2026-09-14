# Q2 — Function with parameters
# Write a function called print_server_info(name, cpu) that takes two parameters 
# and prints something like "Server X has CPU usage of Y%". Call it with at least two different servers to show it's reusable.

def print_server_info(name,cpu):
    print(f"Server {name} has CPU usage of {cpu}%")

usage=print_server_info("AWS1",65)
print(usage)
