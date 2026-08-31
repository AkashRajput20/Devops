# You have user_record = "akash,devops,pune" (a comma-separated line, like you'd get reading a CSV row or a config line).

# Use .split(",") to break it into three separate pieces, and print each one with a label, e.g.:

# Name: akash
# Role: devops
# City: pune

user_record="akash,devops,pune"
x=user_record.split(",")
name1=x[0]
print("Name:",name1)
r1=x[1]
print("Role:",r1)
c1=x[2]
print("City:",c1)



# print(user_record.split(","))
# print(user_record)
# name1=user_record[1]
# print("Name:",name1)

