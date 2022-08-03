# crear una aplicación que obtendrá los elementos impares de una lista 
# pasada por parámetro con filter y realizará una suma de todos estos 
# elementos obtenidos mediante reduce.


def getOdds(nums):
    for num in nums:
        isEven = num % 2 == 0
        if isEven:
            nums.remove(num)
    print (*nums)
    
def addition(nums):
    for num in nums:
        sum  += num
        
