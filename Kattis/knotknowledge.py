# The first line of input consists of an integer, n, the number of knots Sonja needs to learn.
# This is followed by a line containing n distinct integers, the knots that Sonja needs to learn.
# Finally, the last line contains n - 1 distinct integers, the knots that Sonja has learned so far.
# You may assume that each knot Sonja has learned is one of the knots she was supposed to learn.
# Output the number of the remaining knot that Sonja needs to learn.

# Take input
n = int(input())
knots = list(map(int, input().split()))
learned = list(map(int, input().split()))

# Initialize remaining
remaining = 0

# Loop through knots
for knot in knots:
    # Check if knot is not in learned
    if knot not in learned:
        # Set remaining to knot
        remaining = knot
        # Break
        break

# Print remaining
print(remaining)