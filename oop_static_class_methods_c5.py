#Usage of Static and Class methods

class Dog(object): 
    dogs = []

    def __init__(self, name):  
        self.Name = name 
        self.dogs.append(self)

    #decorators
    @classmethod  
    def num_dogs(cls):  #cls (class) is the referecne to class itself. In our case class Dog.
        return(len(cls.dogs))
    
    @staticmethod #Think of them as a regular function that is organized in a class. By doing that you can also call that function on a different python file via import ClassName, then ClassName.function(atr).
    def bark(n):  #beware ne cls or self (instance) is needed..
        #barks n times
        for _ in range(n):
            print('Bark!')



dog1 = Dog('Doggy')
dog2 = Dog('Zeus')

#class method usage
print(Dog.num_dogs()) #you call it on the class (Dog) instead of an object or instance
print(dog1.num_dogs()) #you can call it on objects/instance as previous methods

#static methods usage
print(Dog.bark(5))

