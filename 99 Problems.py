import sys

a = int(sys.stdin.read())
b = a

for i in range (0, 100):
    if a % 100 == 99:
        print(a)
        break
    elif b % 100 == 99 and b > 0:
        print(b)
        break
    a += 1
    b -= 1