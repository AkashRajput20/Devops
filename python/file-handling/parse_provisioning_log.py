# The scenario

# Your nightly M365 user provisioning job writes a log file. Someone needs to know why it keeps partially failing.

# Read the file safely. If the filename is wrong, print a clear message and exit cleanly. No traceback.

# The file we want to read. Kept in a variable so it's easy to change.
filename = 'provisioning.log'

try:
    handle = open(filename)              # open the file, might fail
    raw_lines = handle.readlines()       # get a list, one string per line
    handle.close()                       # good habit: close when done
except FileNotFoundError:
    print("Cannot find " + filename)     # tell the human what went wrong
    exit()                               # stop, don't carry on without data

# Remove the trailing newline from every line
lines = [item.strip() for item in raw_lines]

print("Total lines read: " + str(len(lines)))