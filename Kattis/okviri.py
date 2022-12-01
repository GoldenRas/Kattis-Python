a = [*input()]
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
for i in range(1,len(a)+1):
    if (len(a) != 1):
        if (i % 4 == 0):
            l1.append(".#..")
            l2.append("#.#.")
            l3.append("." + a[i-1] + ".#")
            l4.append("#.#.")
            l5.append(".#..")
        elif (i % 3 == 0):
            l1.append("..*..")
            l2.append(".*.*.")
            l3.append("*." + a[i-1] + ".*")
            l4.append(".*.*.")
            l5.append("..*..")
        elif (i % 2 == 0):
            l1.append("..#.")
            l2.append(".#.#")
            l3.append("#." + a[i-1] + ".")
            l4.append(".#.#")
            l5.append("..#.")
        else:
            l1.append("..#.")
            l2.append(".#.#")
            l3.append("#." + a[i-1] + ".")
            l4.append(".#.#")
            l5.append("..#.") 
    else:
        l1.append("..#..")
        l2.append(".#.#.")
        l3.append("#." + a[i-1] + ".#")
        l4.append(".#.#.")
        l5.append("..#..")
print("".join(l1))
print("".join(l2))
print("".join(l3))
print("".join(l4))
print("".join(l5))
    