nums = []

for num in range(1, 101):
    nums.append(num)
    
sortedNums = sorted(nums, reverse = True)
print(*sortedNums)