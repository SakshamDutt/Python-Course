'''

class Point:
    default_color = 'red' # Class attribute (can be access by Point.default_color/ shared across instances of class)
    def __init__(self,x,y): # ( MAGIC METHODS )Called automatically when creating instance(object)
        self.x = x
        self.y = y
    
    def __str__(self): # ( MAGIC METHOD ) It converts class object automatically to string
        return f"({self.x},{self.y})"

    @classmethod # Decorator (Necessary to tell python that next function arguement is class reference )
    def zero(cls): # cls is class reference
        print(cls(0,0))
        return cls(0,0) 
    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

    def __gt__(self,other):
        return self.x > other.x and self.y > other.y
point = Point(1,2)
# point.draw()
   
# point = Point.zero()   
print(point)

# comparing objects
point = Point(10,22)
other = Point(1,2)
# print(point == other) # OUTPUT: False ( because both instance refer to different addresses in memory)

# After using eq and gt magic method
print(point == other)
print(point> other)

'''
# -------------------------------------------------
# MAKING CUSTOM CONTAINERS


# Custom designed dictionary to limit case sensitive issues
 
class TagCloud: 
    def __init__(self):
        self.__tags = {}

    def add(self,tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self,tag):
        return self.__tags.get(tag.lower(), 0)        

    def __setitem__(self,tag,count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)        
    def __iter__(self):
        return iter(self.__tags)
    
cloud = TagCloud()
# print(cloud.__tags) # Maked tags private by using double underscore
# print(cloud.tags["PYTHON"]) # Gives ERROR to prevent accidental use in the code we make tags a PRIVATE MEMBER


'''
cloud['python'] = 10
print(len(cloud))
print( cloud['python'])
cloud.add('Python')                
cloud.add('python')                
cloud.add('python')
print(cloud.__tags)                '''



class Product:
    def __init__(self,price):
        self.price = price
    
    @property
    def price(self):
        return self.__price        
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative.')
        self.__price = value

    # price = property(get_price, set_price) # (Getter and Sender)

product = Product(10)
print(product.price)

# PROPERTIES --- https://replit.com/@SakshamDutt/LumpyGrowlingHardware#main.py     


# ------------------------------------------------------------------------
# INHERITANCE 

# Every class derive from the main class called Object
class Animal:
    def __init__(self):
        self.age = 1
    def eat(self):
        print('Eat')

class Mammal(Animal):
    def __init__(self):
        super().__init__() # [ PREVENT METHOD OVERRIDING ]  Required to run magic method of parent class 
        self.weight = 2

    def walk(self):
        print('Walk')

class Fish(Animal):
    def swim(self):
        print('Swim')


m = Mammal()
m.eat()

print(issubclass(Mammal,Animal))

print('------------------------------------------------------')

# Multiple Inheritance
class Employee:
    def greet(self):
        print('Employee greet')

class Person:
    def greet(self):
        print('Person greet')

class Manager(Employee,Person):# Greet function is executed of first parent class written in code
    pass

manager = Manager()
manager.greet()


print('------------------------------------------------------')
# Example of good inheritance

from abc import ABC, abstractmethod 

class InvalidOperationError(Exception): # For a custom designed ERROR
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError('Stream is already Opened')
        self.opened = True
    def close(self):
        if not self.opened:
            raise InvalidOperationError('Stream is already Closed')
        self.opened = False
    @abstractmethod # This code had made neccessary for the child class to have read() method to create its instance
    def read(self):
        pass        

class FileStream(Stream):
    def read(self):
        print('Reading data from a file')
class NetworkStream(Stream):

    def read(self):
        print('Reading data from a network')

# stream = Stream()         
# stream.open()


print('------------------------------------------')

from collections import namedtuple

Point = namedtuple('Point', ['x','y']) 
p1 = Point(x=1, y=2) #(Immutable instances)
p2 = Point(x=1, y=2)
print(p1 == p2)