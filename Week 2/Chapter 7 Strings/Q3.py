# You have a messy config value: raw_value = "   production   " (extra spaces around it 
# — common when reading values from config files or user input).

# Use .strip() to remove the extra spaces
# Then use .replace() to turn "production" into "prod"
# Print the final cleaned result

raw_value="  production  "
value1=raw_value.strip()
final_value=value1.replace("production" ,"prod")
print(final_value)

