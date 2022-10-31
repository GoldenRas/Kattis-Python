from calendar import day_name
import sys

input = sys.stdin.read().split()
counter = 0
for i in range(int[input[0]]):
    current = 0
    daytime = input[i + 1 + counter]
    nighttime = input[i + 2 + counter]
    a = input[i + 3 + counter]
    b = input[i + 4 + counter]
    d = input[i + 5 + counter]
    counter += 5
    total = a + 2 * b + d
    isDay = (daytime > a)
    