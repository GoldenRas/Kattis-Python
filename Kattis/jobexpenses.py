n = int(input())
k = input().split()
total = 0

for i in range(n):
    if int(k[i]) < 0:
        total -= int(k[i])
        
print(total)