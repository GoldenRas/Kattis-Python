# The input contains four integers, h, k, v and s.
# h is out starting height, k is a fixed factor, v is the starting velocity, and s is the strength of the wind.
# Output a single integer, which is the distance the aeroplane travels horizontally.

# Take input
import math


h, k, v, s = map(int, input().split())

# Initialize distance
distance = 0

# Loop while h is greater than 0
while h > 0:
    # increase v by s
    v += s
    # decrease v by max(1, v/10 floor)
    v -= max(1, math.floor(v//10))
    # if v >= k add 1 to h
    if v >= k:
        h += 1
    # if 0 < v < k subtract 1 from h
    elif 0 < v < k:
        h -= 1
    # if h is zero after decrease, set v to zero
    if h == 0:
        v = 0
    # if v <= 0 set h and v to zero
    if v <= 0:
        h = 0
        v = 0
    # add v to distance
    distance += v
    # if s > 0 decrease it by 1
    if s > 0:
        s -= 1

# Print distance
print(distance)