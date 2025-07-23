excluded_problems = 0
for _ in range(int(input())):
    if int(input()) % 2 != 0:
        excluded_problems += 1
print(excluded_problems)