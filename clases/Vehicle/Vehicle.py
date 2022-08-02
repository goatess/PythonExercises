class Vehicle:
    wheels = 0
    color = None
    doors = 0

    def __init__(self, wheels, color, doors):  # constructor
        self.wheels = wheels
        self.color = color
        self.doors = doors

    def __del__(self):  # destructor
        pass
