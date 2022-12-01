a = sorted(map(int, input().split()))
d = [*input()]
nums = []
for i in range(len(d)):
    if d[i] == "A":
        nums.append(a[0])
    if d[i] == "B":
        nums.append(a[1])
    if d[i] == "C":
        nums.append(a[2])
print(nums[0], nums[1], nums[2])