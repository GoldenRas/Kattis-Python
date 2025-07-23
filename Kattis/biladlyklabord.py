result = []
for char in input():
    if not result or char != result[-1]:
        result.append(char)
print(''.join(result))