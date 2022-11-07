n = list(input())
last = ''
hiss = False

for i in range(len(n)):
    if last == 's' and n[i] == 's':
        hiss = True
    last = n[i]

if hiss:
    print("hiss")
else:
    print("no hiss")