a = set(input())
b = input()
count = 0

for character in b:
    if not a:
        print('WIN')
        break
    elif count == 10:
        print('LOSE')
        break
    elif character in a:
        a.remove(character)
    else:
        count += 1