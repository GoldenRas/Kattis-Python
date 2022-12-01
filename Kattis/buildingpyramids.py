import sys

ab = int(sys.stdin.read())
length = 1
counter = 0

while ab > 0:
    ab = ab - (length * length)
    if ab >= 0:
        counter = counter + 1
    length = length + 2
    
print(counter)