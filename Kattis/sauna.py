n = int(input())
low, high = 0, int(1e9)

for _ in range(n):
    a, b = map(int, input().split())
    low = max(low, a)
    high = min(high, b)

if low > high:
    print("bad news")
else:
    print(high - low + 1, low)