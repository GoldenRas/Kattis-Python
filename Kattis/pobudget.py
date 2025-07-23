total = 0
for i in range(int(input())):
    # Discard Line
    input()
    total = total + int(input())

if total < 0:
    print("Nekad")
elif total == 0:
    print("Lagom")
else:
    print("Usch, vinst")