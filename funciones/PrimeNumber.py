def isPrime(number):
    for num in range(2, number):
        if number % num == 0:
            print(number, "No es primo", num, "es divisor de", number)
            return False
    print(number, "Es primo")
    return True

isPrime(2)
isPrime(13)
isPrime(101)
isPrime(1001)