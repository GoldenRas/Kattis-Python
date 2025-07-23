from collections import deque, defaultdict

print("--- Day 5: Print Queue ---")

def is_orderered(update, cache):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            key = (update[i], update[j])
            if key in cache and not cache[key]:
                return False
    return True
def topological_sort(nodes, edges):
    graph = defaultdict(list)
    in_degree = {node: 0 for node in nodes}

    for x, y in edges:
        if x in nodes and y in nodes:
            graph[x].append(y)
            in_degree[y] += 1
    queue = deque([node for node, degree in in_degree.items() if degree == 0])
    sorted_list = []

    while queue:
        current = queue.popleft()
        sorted_list.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_list

def part1():
    file = open('input/day5.txt')
    rules = []

    for line in file:
        if line.isspace(): break
        rules.append(list(map(int, line.split('|'))))

    cache = {}

    for x,y in rules:
        cache[(x,y)] = True
        cache[(y,x)] = False
    total = 0
    for line in file:
        update = list(map(int, line.split(',')))
        if is_orderered(update, cache):
            total += update[len(update) // 2]

    return total


def part2():
    file = open("input/day5.txt")
    rules = []

    for line in file:
        if line.isspace(): break
        rules.append(list(map(int, line.split('|'))))

    cache = {}

    for x, y in rules:
        cache[(x, y)] = True
        cache[(y, x)] = False
    total = 0
    for line in file:
        update = list(map(int, line.split(',')))
        if not is_orderered(update,cache):
            sorted = topological_sort(update, rules)
            total += sorted[len(sorted) // 2]

    return total

print("Part 1: " + str(part1()))
print("Part 2: " + str(part2()))