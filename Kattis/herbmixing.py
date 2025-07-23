green_herbs, red_herbs = map(int, input().split())
health_boost = 0
for i in range(green_herbs):
    if red_herbs > 0:
        red_herbs -= 1
        health_boost += 10
    elif green_herbs - i >= 3:
        health_boost += 10
        green_herbs -= 2
    elif green_herbs - i >= 2:
        health_boost += 3
        green_herbs -= 1
    elif green_herbs - i >= 1:
        health_boost += 1

print(health_boost)