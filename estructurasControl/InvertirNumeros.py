
nums = []
num = 1
while num <= 100:
    nums.append(num)
    num += 1
    
sortedNums = sorted(nums, reverse = True)
print(*sortedNums)