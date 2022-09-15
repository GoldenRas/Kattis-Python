import sys
inp = sys.stdin.read()
last_letter = ''
lst = []
lst.extend(inp)
output = ""
for i in lst:
    if last_letter != i:
        output = output + i
    last_letter = i
print(output)