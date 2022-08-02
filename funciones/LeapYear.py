
def isLeap(year):
    if is4Mult(year):
        if is100Mult(year) and not is400Mult(year):
            return False    
        return True
    else: 
        return False 

def is100Mult(year):
    return year % 100 == 0

def is400Mult(year):
    return year % 400 == 0

def is4Mult(year):
    return year % 4 == 0   
    
print(isLeap(2019))  # expected False
print(isLeap(2020))  # expected True
print(isLeap(2100))  # expected False
print(isLeap(2000))  # expected True