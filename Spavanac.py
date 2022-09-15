import sys

inp = sys.stdin.read().split(" ")

if int(inp[1]) > 44:
    inp[1] = int(inp[1]) - 45
    print(str(inp[0]) + " " + str(inp[1]))
else:
    if inp[0] == "0":
        inp[0] = 23
    else:
         inp[0] = int(inp[0]) - 1
    
    inp[1] = int(inp[1]) + 15
    print(str(inp[0]) + " " + str(inp[1]))