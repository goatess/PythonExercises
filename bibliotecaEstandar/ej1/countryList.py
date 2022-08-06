# Crea un script que le pida al usuario una lista de países (separados por comas). 
# Éstos se deben almacenar en una lista.
# No debería haber países repetidos (haz uso de set). Finalmente, muestra por 
# consola la lista de países ordenados alfabéticamente y separados por comas.

def splitList(countries):
    countries = countries.split(', ')
    return countries

def sortList(countries):
    return sorted(countries)

def filterList(countries):
    return set(countries)

countries = splitList('Francia, Italia, Grecia, Francia')
countries = filterList(countries)
countries = sortList(countries)
print(countries)

    