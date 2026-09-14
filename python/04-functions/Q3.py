# Q3 — Fruitful function (returns a result)
# Write a function called is_over_threshold(value, threshold) that returns True if value > threshold, 
# otherwise False — don't print inside the function, just return the result. 
# Then call it and print the result outside the function, e.g., print(is_over_threshold(92, 90)).

def is_over_threshold(value , threshold):
    compare=value > threshold
    return compare
result=is_over_threshold(99 ,112)
print(result)
