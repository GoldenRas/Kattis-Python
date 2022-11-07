for _ in range(int(input())):
    k, n = map(int, input().split())
    v = n*(n+1)
    print(k, v//2, n**2, v)