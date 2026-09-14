# Q4 — Handling a file that might not exist

# Try opening a file called does_not_exist.txt, wrapped in try/except, 
# so instead of crashing it prints "File not found, please check the path".

try:
    gcps1=open("does_not_exist.txt")
    print(gcps1)
except FileNotFoundError:
    print("File not found")
    (exit)