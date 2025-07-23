for _ in range(int(input())):
    current_number = int(input())
    result = ""
    if current_number % 2 != 0:
        result += "O"
    if current_number ** 0.5 == int(current_number ** 0.5):
        result += "S"
    print(result if result else "EMPTY")