# Take input from first line as two ints, n and m.
# The next n lines will contain ints that must be added.
# If the sum of the ints is greater than m, print "Neibb", else print "Jebb".

# Take input
n, m = map(int, input().split())

# Initialize sum
sum = 0

# Loop through n times
for i in range(n):
    # Add the input to sum
    sum += int(input())

# Check if sum is greater than m
if sum > m:
    # Print "Neibb"
    print("Neibb")
else:
    # Print "Jebb"
    print("Jebb")

