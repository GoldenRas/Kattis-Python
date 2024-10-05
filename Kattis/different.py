# Write a program that computes the difference between non-negative integers.

# Input
# Each line of the input consists of a pair of integers. Each integer is between 0 and 1015 (inclusive). The input is terminated by end of file.

# Output
# For each pair of integers in the input, output one line, containing the absolute value of their difference.

# Input
a, b = map(int, input().split())
while a != None and b != None:
    print(abs(a-b))
    try:
        a, b = map(int, input().split())
    except:
        break