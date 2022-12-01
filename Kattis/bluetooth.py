lu = 0
ll = 0
ru = 0
rl = 0
for _ in range(int(input())):
    a, b = input().split()
    c, d = [*a]
    if(b == "b"):
        if (d == "-"):
            rl += 10
        elif (d == "+"):
            ru += 10
        elif (c == "-"):
            ll += 10
        elif (c == "+"):
            lu += 10
    else:
        if (d == "-"):
            rl += 1
        elif (d == "+"):
            ru += 1
        elif (c == "-"):
            ll += 1
        elif (c == "+"):
            lu += 1
if (ru < 8 and rl < 8):
    print("1")
elif (lu < 8 and ll < 8):
    print("0")
else:
    print("2")