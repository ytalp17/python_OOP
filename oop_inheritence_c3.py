#Inheritence


class Dog(object): #self represents the instance itself.
    def __init__(self, name, age):  #this is called automatically as soon as an object is created!
        self.Name = name # an example of an class attribute
        self.Age = age

    def speak(self): 
        print('Hi! My name is ', self.Name) 

    def talk(self):
        print('Bark!')

#class Cat(object):
#    def __init__(self,name, color, age) -> None:
#        self.Name = name # an example of an class attribute
#        self.Age = age
#        self.Color = color
#    
#    def speak(self): 
#        print('Hi! My name is ', self.Name, ', and I am a dog, wooou!') 


class Cat(Dog): #Dog is the parent class and Cat inherts form the Dog class. You can get the same result with the above chunk of code
    def __init__(self, name, age, color):
        super().__init__(name, age) #super class here simply means the Dog class. the line of code means get the init method of the class.
        self.Color = color

    def talk(self): #Overrides the talk method that we inherited from the Dog class!
        print('Meow!')



#Sara = Cat('Sara', 12, 'grey')
#print(Sara.Color)
#Sara.talk()


class Vehicle():
    def __init__(self, price, gas, color) -> None:
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0
    
    def gasLeft(self):
        return self.gas
    
class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed
    
    def beep(self):
        print("Beep beep")

class Truck(Vehicle):  #you can also take inheritence from class car since it is already had inherited from class Vehicle -> class Truck(Car):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires
    
    def beep(self):
        print("Honk honk")

