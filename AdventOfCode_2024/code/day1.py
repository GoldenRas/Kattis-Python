from collections import Counter

with open("input/day1.txt", "r") as f:
    data = f.read().splitlines()
    list1 = []
    list2 = []
    for line in data:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)
    list1.sort()
    list2.sort()

    total_distance = sum(abs(a - b) for a, b in zip(list1, list2))
    print(total_distance)

    counter = Counter(list2)
    similarity_score = sum(num * counter[num] for num in list1)
    print(similarity_score)