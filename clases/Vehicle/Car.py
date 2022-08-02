from Vehicle import Vehicle

class Car(Vehicle):  # Car inherits Vehicle 
    speed = 0
    cc = 0
    
    def __init__(self, speed, cc, wheels, color, doors):  # constructor of child class 
        # calls constructor of parent class
        # Vehicle.__init__(self, wheels, color, doors)      
        super().__init__(wheels, color, doors) 
        self.wheels = wheels
        self.color = color
        self.doors = doors           
        self.speed = speed
        self.cc = cc
    
    