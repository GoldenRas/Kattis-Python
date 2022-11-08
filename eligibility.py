for _ in range(int(input())):
    n = input().split()
    y, _, _ = n[1].split("/")
    if (2009 < int(y)):
        print(n[0], "eligible")
        continue
    elif (1990 < int(n[2].split("/")[0])):
        print(n[0], "eligible")
        continue
    elif (40 < int(n[3])):
        print(n[0], "ineligible")
        continue
    else:
        print(n[0], "coach petitions")