def is_valid_number(n):
    digits = [int(d) for d in str(n)]
    if len(digits) != len(set(digits)) or 0 in digits:
        return False
    for d in digits:
        if n % d != 0:
            return False
    return True

def count_valid_combinations(L, H):
    valid_count = 0
    for n in range(L, H + 1):
        if is_valid_number(n):
            valid_count += 1
    return valid_count

L, H = map(int, input().split())
print(count_valid_combinations(L, H))
