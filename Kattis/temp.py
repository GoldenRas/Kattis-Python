N,P = map(int, input().split())

# Remove initial space from total sweater
R = N - P
# Divide sweater into equal parts
HR = R / 2
# Find remaining space on either side
SL = HR % P
# If space is perfectly fitting for extra full pattern, add it
if (SL == P / 2):
    SL = 0
# Print total space left
total = 2 * SL

print(int(total))