import math
while True:
    r, m, c = list(input().split())
    if (r == "0" and m == "0" and c == "0"):
        break
    area = math.pi*float(r)**2
    percentage = 4 * int(c) / int(m) * float(r) * float(r)
    print(area, percentage)