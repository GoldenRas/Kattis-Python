n,m=map(int,input().split())
counter, current = 0, 0
for i in range(m):
    b,c = input().split(" ")
    if (b[0] == "e"):
        if (int(c) + current <= n):
            current += int(c)
        else:
            counter += 1
    else:
            current -= int(c)
print(counter)