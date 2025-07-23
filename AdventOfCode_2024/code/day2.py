safe = 0
with open("input/day2.txt", "r") as f:
    data = f.read().splitlines()
    for line in data:
        p = map(int, line.split())
        levels = list(p)
        if all(1 <= abs(levels[i] - levels[i-1]) <= 3 for i in range(1, len(levels))):
            if all(levels[i] > levels[i-1] for i in range(1, len(levels))) or all(levels[i] < levels[i-1] for i in range(1, len(levels))):
                safe += 1

print(safe)

safe = 0

def is_safe(levels):
    return all(1 <= abs(levels[i] - levels[i-1]) <= 3 for i in range(1, len(levels))) and (
        all(levels[i] > levels[i-1] for i in range(1, len(levels))) or 
        all(levels[i] < levels[i-1] for i in range(1, len(levels)))
    )

for line in data:
    p = map(int, line.split())
    levels = list(p)
    if is_safe(levels):
        safe += 1
    else:
        for i in range(len(levels)):
            if is_safe(levels[:i] + levels[i+1:]):
                safe += 1
                break

print(safe)