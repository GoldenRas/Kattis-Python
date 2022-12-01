import sys

ab = int(sys.stdin.read())

a = 100 / ab
print(a)
ab = 100 / (100 - ab)
print(ab)