import sys

inp = sys.stdin.read().split()

for i in range (1, int(inp[0]) + 1):
    if int(inp[i]) % 2 == 0:
        print(inp[i] + " is even")
    else:
        print(inp[i] + " is odd")