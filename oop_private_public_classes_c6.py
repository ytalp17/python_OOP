

class _Private:  #sytnex has a one underscore at the begining of the class name as a convention. It basically signals other programmers to dont mess with this class :) 
    def __init__(self, name):
        self.name = name

class Public:
    def __init__(self, name):
        self.name = NameError
        self.priv = _Private(name)

    def _display(self): #private method. Yes methods can be private as well!
        print('hello')

    def display(self):
        print("hi")


        
