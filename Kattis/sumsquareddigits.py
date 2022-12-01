for _ in range(int(input())):
    k, b, n = map(int,input().split())
    total = 0
    while(n > 0):
        a = n % b
        total += a**2
        n -= a
        n //= b
    print(k, total)