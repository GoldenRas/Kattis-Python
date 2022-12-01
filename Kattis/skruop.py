n = int(input())
count = 7
for _ in range(n):
    k = input()
    if k == "Skru op!" and count < 10:
        count += 1
    elif k == "Skru ned!" and count > 0:
        count -= 1
print(count)