from math import ceil, log2
import sys

ab = sys.stdin.read().split()
a = int(ab[0])
b = int(ab[1])

if((int(ceil(log2(a)) + ceil(log2(b))) % 2)):
    print("A")
else:
    print("B")