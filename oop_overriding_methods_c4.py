#Overriding Methods


#Let's define couple of builtin methods inside of the Point Class.
# __('Name')__ is the general syntax for builtin (predefined) functions.. A.K.A Underscore methods

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
    
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    
    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)
    
    def __gt__(self, p):
        return self.length() >  p.length() #returns bool value .. 

    def __ge__(self, p):
        return self.length() >=  p.length() #..

    def __lt__(self, p):
        return self.length() <  p.length()

    def __le__(self, p):
        return self.length() <=  p.length()

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y
    

        

#Define random points
p1 = Point(3,4)
p2 = Point(3,2)

# arithmatic operations
print('sum', p1 + p2)
print('p1>p2 ', p1==p2)


# you can see all the predefined functions on python by using CL command egrep -oh '__[A-Za-z_][A-Za-z_0-9]*__' *.py | sort | uniq
# under /Lib directory 