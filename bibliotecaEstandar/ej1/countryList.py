# Crea un script que le pida al usuario una lista de países (separados por comas). 
# Éstos se deben almacenar en una lista.
# No debería haber países repetidos (haz uso de set). Finalmente, muestra por 
# consola la lista de países ordenados alfabéticamente y separados por comas.

def split(countries):
    countries = countries.split(', ')
    return countries

def sort(countries):
    countries = countries.sort()
    return countries

def filter(countries):
    countriesSet = {}
    countriesSet = set(countries)
    return countriesSet

countries = split('uno, dos, tres')
countries = sort(countries)
print(filter(countries))  

    