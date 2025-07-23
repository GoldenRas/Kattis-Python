hungover = 0
last_night = ""
for _ in range(int(input())):
    tonight = input()
    if tonight == "sober" and last_night == "drunk":
        hungover += 1
    last_night = tonight
print(hungover)
