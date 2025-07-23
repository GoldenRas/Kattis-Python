def solve():
    n, r, c = map(int, input().split())
    rows = [input().split() for _ in range(r)]
    attendance = [input().strip() for _ in range(n)]
    attendance_index = {name: i for i, name in enumerate(attendance)}

    for row in rows:
        indices = [attendance_index[name] for name in row]
        if indices == sorted(indices):
            print("left")
        else:
            print("right")

solve()
