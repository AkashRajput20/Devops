# # Q3 — Loop idiom (finding the max)
# # Write a script with a list of CPU usage values: [45, 78, 92, 60, 88]. Use a for loop to find and print the highest value
# # but don't use Python's built-in max() function. Build the "largest so far" logic yourself, 
# since that's the actual idiom this chapter is teaching.

largeest_so_far= 45
print(largeest_so_far)
for num in [45, 78, 92, 60, 88]:
    if num > largeest_so_far:
        largeest_so_far =num
        print(largeest_so_far , num)
print(largeest_so_far)        
   
