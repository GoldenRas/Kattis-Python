def count_deathknight_wins(n, battles):
    count = 0
    for battle in battles:
        if 'CD' not in battle:
            count += 1
    return count

if __name__ == "__main__":
    n = int(input())
    battles = [input().strip() for _ in range(n)]
    result = count_deathknight_wins(n, battles)
    print(result)