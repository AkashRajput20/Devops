# Q4 — try/except

# Write a script that tries to convert value = "abc" into an integer using int(value).
#  Wrap it in try/except so that if the conversion fails, it prints "Invalid number format" instead of crashing.


value="42"
try:
    print(int(value))
except:    
    print("Invalid number format")