# crear una aplicación que obtendrá los elementos impares de una lista 
# pasada por parámetro con filter y realizará una suma de todos estos 
# elementos obtenidos mediante reduce.

def check(number):
    if number % 2 != 0:
        return True
    else: 
        return False
        
def addition(numbersList):
    sum = 0
    for number in numbersList:
        sum += number
    return sum
      
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odds = list(filter(check, numbers))
print(odds)
print(addition(odds))
