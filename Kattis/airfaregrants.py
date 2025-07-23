def calculate_airfare_grant():
    flights = [int(input()) for _ in range(int(input()))]
    price = min(flights) - max(flights) // 2
    print(max(0, price))

if __name__ == "__main__":
    calculate_airfare_grant()