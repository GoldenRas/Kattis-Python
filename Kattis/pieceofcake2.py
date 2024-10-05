# A cake is 4 cm high.
# Three ints are given as input.
# The first, n, is the length of the sides of the cake.
# The second, h, is the distane of the horizontal cut from the top of the cake.
# The third, v, is the distance of the vertical cut from the left side of the cake.
# The output should be the volume of the largest piece of cake.

# Take input
n, h, v = map(int, input().split())

# Initialize volume
volume = 1

# Check if h is greater than n/2
if h > n/2:
    # Set volume to volume * h
    volume *= h
else:
    # Set volume to volume * (n - h)
    volume *= (n - h)

# Check if v is greater than n/2
if v > n/2:
    # Set volume to volume * v
    volume *= v
else:
    # Set volume to volume * (n - v)
    volume *= (n - v)

# Print volume * 4
print(volume * 4)