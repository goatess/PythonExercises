import pickle 
import vehicle

car = vehicle.Vehicle("red")
file = open('entradaSalida/ej2/car.bin', 'wb')
pickle.dump(car, file)
file.close()
print(car.color)

file = open('entradaSalida/ej2/car.bin', 'rb')
car = pickle.load(file)
file.close()
print(car.color)
