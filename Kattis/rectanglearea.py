a,b,c,d = map(float, input().split())

ac = abs(a - c)
bd = abs(b - d)
print(f"{ac * bd:.3f}")