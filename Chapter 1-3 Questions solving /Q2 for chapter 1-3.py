# Q2 — Type checking
# Create a variable disk_usage = "85" (as a string, on purpose). Print its type using type().
#  Then convert it to an integer using int() and print the new type.
#  Why does this conversion matter in real scripts? (Answer in a comment in your code.)

#code build by myself 
# disk_usage="85"
# print type(int)
# int disk_usage=85
# print(disk_usage)
#converion is required beacuse the disk usage should br in integer form not in char

#corrrect code 
disk_usage="85"
print(type(disk_usage))
disk_usage=int(disk_usage)
print(disk_usage)
