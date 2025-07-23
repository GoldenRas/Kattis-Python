from math import cos, sin, radians
t = int(input())
for i in range(t):
    v0, theta, x1, h1, h2 = map(float, input().split())
    t_impact = x1/(v0 * cos(radians(theta)))
    y_impact = v0 * t_impact * sin(radians(theta)) - 0.5*9.81*((t_impact)**2)
    if y_impact+1 < h2 and y_impact-1 > h1:
        print("Safe")
    else:
        print("Not Safe")