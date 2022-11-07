n = int(input())
p = int(input())

length = 0
for i in range( p-1, -1, -1 ):
    w, h = (int(x) for x in input().split())
    length += w * h
print(int(length/n))