from collections import Counter

cities = [input() for _ in range(int(input()) * 2)][1::2]
city_counts = Counter(cities)
for city, count in city_counts.items():
    print(f"{city} {count}")
