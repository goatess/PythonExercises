
nums = [0,1,2,3,4,5,6,7,8,9]
for num in nums:
    isEven = num % 2 == 0
    if isEven:
        nums.remove(num)
print (*nums)
