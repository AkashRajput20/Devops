# Q3 — Expressions with modulo

# Write a script that:

# Stores total_servers = 17
# Stores batch_size = 5
# Uses the % (modulo) operator to calculate how many servers would be "left over" if you split them into batches of 5
# Prints the result using an f-string, e.g., something like: "17 servers split into batches of 5 leaves X servers remaining"

server=17
print(type(server))
batch_size=5
print(type(batch_size))
left_over=server%batch_size
print(f"17 servers split into batches of 5 leaves {left_over} servers remaining")