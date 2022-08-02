import pickle 
import vehicle

car = vehicle.Car("red")
file = open('entradaSalida/car.bin', 'wb')
pickle.dump(car, file)
file.close()
print(car.color)

file = open('entradaSalida/car.bin', 'rb')
car = pickle.load(file)
file.close()
print(car.color)