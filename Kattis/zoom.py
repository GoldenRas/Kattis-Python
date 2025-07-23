a, b = map(int, input().split())
c = input().split()
result = [c[i] for i in range(b - 1, a, b)]
print(" ".join(result))
