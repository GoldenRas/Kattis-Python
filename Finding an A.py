import sys

a = sys.stdin.read()
index = a.find('a')
if index != -1:
    result = a[index:]
else:
    result = a

print(result)
    