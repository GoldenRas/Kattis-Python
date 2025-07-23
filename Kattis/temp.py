n = int(input())
best = []

while n > 0:
    best.append("2" if n % 3 else "3")
    n -= 2 if n % 3 else 3

print(len(best))
print(" ".join(best))

N,P = map(int, input().split())

# Remove initial space from total sweater
R = N - P
# Divide sweater into equal parts
HR = R // 2
# Find remaining space on either side
SL = int(HR) % int(P)
# If space is perfectly fitting for extra full pattern, add it
if (int(SL) == int(P) // 2):
    SL = 0
# Print total space left
total = 2 * int(SL)

print(int(total))