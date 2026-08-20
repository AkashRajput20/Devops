# Q2 — While loop with a counter
# Write a while loop that starts a counter at 0, and keeps printing "Retry attempt: X" while the counter is less than 5.
#  Make sure to increment the counter inside the loop, otherwise think about what happens.

n=0
while n < 5:#while n > 0:
    # print(n)
    n=n+1
    print("Retry attempt:" , n)