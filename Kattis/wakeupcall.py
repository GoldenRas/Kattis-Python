a = map(int,input().split())
b = sum(map(int,input().split()))
c = sum(map(int,input().split()))

if b == c:
    print("Oh no")
elif b > c:
    print("Button 1")
else:
    print("Button 2")