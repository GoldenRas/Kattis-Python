n, p, s = map(int, input().split())

for _ in range(s):
    remove = False
    b = list(input().split(" "))
    for i in b[1:]:
        if (int(i)) == p:
            remove = True
    if remove:
        print("KEEP")
    else:
        print("REMOVE")
        