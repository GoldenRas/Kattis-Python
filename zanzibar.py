for _ in range(int(input())):
    total = 0
    k = list(map(int,input().split()))
    for i in range(len(k)-1):
        change = k[i+1] - k[i]*2
        if (change > 0):
            total += change
    print(total)