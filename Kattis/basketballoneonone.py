a, b = 0, 0
c = input()

for i in range(1, len(c), 2):
    player = c[i-1]
    points = int(c[i])
    
    if player == 'A':
        a += points
    else:
        b += points
    
    if a >= 11 and a - b >= 2:
        print("A")
        break
    elif b >= 11 and b - a >= 2:
        print("B")
        break
