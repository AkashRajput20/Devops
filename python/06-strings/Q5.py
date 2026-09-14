# Q5 — Mini scenario: username validation

# Write a check for username = "Admin_User123".

# Using .lower(), in, and len(), check and print whether the username:

# (a) is at least 8 characters long
# (b) contains the word "admin" if you first convert it to lowercase

# Print a clear message for each check, e.g.:

# Length check: Passed
# Contains 'admin': Yes


username="Admin_User123"
index=8
if len(username) >=index:
    print("Length check: Passed")
else:
     print("Length check: Failed")

if "admin" in username.lower():
      print("Contains 'admin': Yes")
else:
     print("Contains 'admin': No")
     
    
    