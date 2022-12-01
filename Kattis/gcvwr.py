import sys

ab = sys.stdin.read().split()
a = int(ab[0])
b = int(ab[1])
c = int(ab[2])
a = a - b
sum = 0
for i in range (3, c + 3):
    sum = sum + int(ab[i])

a = a * 0.9 - sum


print(int(a))