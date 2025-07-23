m, n = list(map(int,input().split()))
for i in range(m):
    c = list(map(int,input().split()))

print("unsatisfactory" if m<8 else "satisfactory")