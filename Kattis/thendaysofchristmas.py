a = int(input())
sum = 0
print((a * (a + 1)) // 2)
for i in range(a + 1):
    sum += (i * (i + 1)) // 2
print(sum)