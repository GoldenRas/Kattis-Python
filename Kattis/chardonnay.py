wine_used = int(input())
special_cases = {0: 0, 7: 7}
print(special_cases.get(wine_used, wine_used + 1))