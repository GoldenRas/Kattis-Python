s = list(input())
a = input()
b = [int(a[i:i+3]) for i in range(0, len(a), 3)]
k = ""
for i in range(len(b)):
    k += s[b[i] - 1]
print(k)