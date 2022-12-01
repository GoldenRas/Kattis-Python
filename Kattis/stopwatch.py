k = [int(input()) for _ in range(int(input()))]
running = False
last_run = k[0]
current_run = 0
total = 0
for i in range(len(k)):
    current_run = k[i]
    if (running):
        total += current_run - last_run
    last_run = current_run
    running = not running
if (not running):
    print(total)
else:
    print("still running")
