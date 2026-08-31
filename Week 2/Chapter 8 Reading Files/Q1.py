# Q1 — Open and read a file, line by line
# Write a script that opens sample_log.txt and prints every line in it, 
# using a for loop (the pattern from your chapter summary — "reading a file line by line with a for loop").


log_web1=open("sample_log.txt")
for line in log_web1:
    xlog=log_web1.read()
    print(xlog)