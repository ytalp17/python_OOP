#creating classes

##You can think of classes as a blueprint for creating an object out of it!

##methods and atributes are used while creating a class



class Dog(object): #self represents the instance itself.
    def __init__(self, name):  #this is called automatically as soon as an object is created!
        self.Name = name # an example of an class attribute
        print('Nice! You just created a dog')

    def speak(self): 
        print('Hi! My name is ', self.Name, ', and I am a dog, wooou!') 

    def add_weight(self, weight):
        self.Weight = weight


doggy = Dog('Doggy') # Doggy is an instance of class Dog. In other words, doggy is Dog object where the self is equal to itself, a.k.a Doggy.

print(doggy.Name) #attributes can be reached as here without calling the methods where they belong to.

doggy.speak()

doggy.add_wright(32)
print(doggy.Weight, "kg")

