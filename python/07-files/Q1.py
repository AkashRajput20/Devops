# Q1 — Open and read a file, line by line

# Write a script that opens sample_log.txt and prints every line in it, using a for loop.

# Save it as q1.py in the same folder as sample_log.txt, and cd there before running.



aws1_logs = open ("sample_log.txt")
for line in aws1_logs:
    print(line.strip())
