a = int(input())
b = int(input())
c, d = divmod(b, a)

for i in range(a):
    e = c + 1 if d > 0 else c
    print(e * "*")
    d -= 1
