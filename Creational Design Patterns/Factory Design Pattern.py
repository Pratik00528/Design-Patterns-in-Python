'''
Factory Design Pattern : 
Factory Method is a creational design pattern that provides an interface for creating objects
in a superclass, but allows subclasses to alter the type of objects that will be created.
 
Problems that arise if we do not use Factory Design Pattern:
Imagine that you’re creating a logistics management application. The first version  of your app 
can only handle transportation by trucks, so the bulk of your code lives inside the Truck class.
After a while, your app becomes pretty popular. Each day you receive dozens of requests from sea 
transportation companies to incorporate sea logistics into the app. Great news, right? 
But how about the code? At present, most of your code is coupled to the Truck class. Adding Ships
into the app would require making changes to the entire codebase. Moreover, if later you decide to
add another type of transportation to the app, you will probably need to make all of these changes again.
As a result, you will end up with pretty nasty code, riddled with conditionals that switch the app’s 
behavior depending on the class of transportation objects.
 
So the above Problem can be solved using Factory Design Pattern:
The Factory Method pattern suggests that you replace direct object construction calls with calls to a special factory method.
 
'''
 
from abc import ABC, abstractmethod
 
# ShapeInterface, it will have an abstract method called draw, and different 
# type of shape objects implements this draw method.
 
class ShapeInterface(ABC):
    @abstractmethod
    def draw(self):
        pass 
# Concrete Circle Class implements our ShapeInterface
class Circle(ShapeInterface):
    def draw(self):
        print("Draw Circle")
# Concrete Square Class implements our ShapeInterface
class Square(ShapeInterface):
    def draw(self):
        print("Draw Square")
# Concrete Rectangle Class implements our ShapeInterface
class Rectangle(ShapeInterface):
    def draw(self):
        print("Draw Rectangle")
# Client Code 
circleObj = Circle()
circleObj.draw() # Prints "Draw Circle"
squareObj = Square()
squareObj.draw() # Prints "Draw Square"
rectangleObj = Rectangle()
rectangleObj.draw() # Prints "Draw Rectangle"
 
# Here the client code creates the objects but that should not be the case i.e. Client shouldn't  
# be responsible for creating objects
 
 
# Now we use "ShapeFactory" which is factory class which will be responsible
# to create objects based on the type of the object.
 
from abc import ABC, abstractmethod
 
# ShapeInterface, it will have an abstract method called draw, and different 
# type of shape objects implements this draw method.
 
class ShapeInterface(ABC):
    @abstractmethod
    def draw(self):
        pass 

 
# Concrete Circle Class implements our ShapeInterface
class Circle(ShapeInterface):
    def draw(self):
        print("Draw Circle")
# Concrete Square Class implements our ShapeInterface
class Square(ShapeInterface):
    def draw(self):
        print("Draw Square")
# Concrete Rectangle Class implements our ShapeInterface
class Rectangle(ShapeInterface):
    def draw(self):
        print("Draw Rectangle")
# ShapeFactory Class
class ShapeFactory:
    # Here we declare this method as static, to make it accessible by using ShapeFactory class. 
    @staticmethod
    def getShape(type = None):
        # If type is equal to "Circle", it should return Circle object
        if type == "Circle":
            return Circle()
        # If type is equal to "Square", it should return Square object
        if type == "Square":
            return Square()
        # If type is equal to "Rectangle" it should return Rectangle object
        if type == "Rectangle":
            return Rectangle()
        return None # Else return None
# Client Code 
circleObj = ShapeFactory.getShape("Circle") 
circleObj.draw() # Prints "Draw Circle" 
squareObj = ShapeFactory.getShape("Square")
squareObj.draw() # Prints "Draw Square"
rectangleObj = ShapeFactory.getShape("Rectangle")
rectangleObj.draw() # Prints "Draw Rectangle"