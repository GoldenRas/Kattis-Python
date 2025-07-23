curr_max = 0
curr_passengers = 0
for _ in range(int(input())):
    leaving, boarding = map(int, input().split())
    curr_passengers += boarding - leaving
    curr_max = max(curr_passengers, curr_max)
print(curr_max)