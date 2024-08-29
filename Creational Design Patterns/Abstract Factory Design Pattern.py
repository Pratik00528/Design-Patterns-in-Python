'''
Abstract Factory Design Pattern:
 
--- Basically Abstract Factory means Factory of factories.
--- Abstract Factory pattern is almost similar to Factory Pattern and is considered as
another layer of abstraction over factory pattern.
--- Abstract Factory patterns work around a super-factory which creates other factories.
--- Abstract factory pattern implementation provides us with a framework that allows us
to create objects that follow a general pattern.
--- So at runtime, the abstract factory is coupled with any desired concrete factory which 
can create objects of the desired type.
 
So in the below example, we have a CarInterface which will be implemented by four concrete class cars i.e.
RangeRoverSUV, VolvoSUV, BenzSedan, AudiSedan.
And we will have two factories - SUVFactory, SedanFactory which will tell which concrete car object
to create based on the car company.
And to choose between these two factories we will have an another factory called CarTypeFactory
which we return Factory object i.e. either SUVFactory or SedanFactory based on the car type.
So this is called Abstract Factory pattern.
 
'''
 
from abc import ABC, abstractmethod
 
# Car Interface, which will be implemented by concrete Car classes
class CarInterface(ABC):
    @abstractmethod
    def display(self):
        pass 
# Concrete Car RangeRoverSUV implements CarInterface
class RangeRoverSUV(CarInterface):
    def display(self):
        print("This is a RangeRover SUV")
# Concrete Car VolvoSUV implements CarInterface
class VolvoSUV(CarInterface):
    def display(self):
        print("This is a Volvo SUV")
 
# Concrete Car BenzSedan implements CarInterface
class BenzSedan(CarInterface):
    def display(self):
        print("This is a Benz Sedan")
 
# Concrete Car AudiSedan implements CarInterface
class AudiSedan(CarInterface):
    def display(self):
        print("This is a Audi Sedan")

 
# SUVFactory which will return concrete SUV car objects
class SUVFactory:
    # Here we declare this method as static, to make it accessible by using SUVFactory class.
    # And this method will return Concrete SUV car objects based on company type.
    @staticmethod
    def getCar(company = None):
        if company == "RangeRover":
            return RangeRoverSUV()
        if company == "Volvo":
            return VolvoSUV()
        return None
# SedanFactory which will return concrete Sedan car objects
class SedanFactory:
    # Here we declare this method as static, to make it accessible by using SedanFactory class.
    # And this method will return Concrete Sedan car objects based on company type.
    @staticmethod
    def getCar(company = None):
        if company == "Benz":
            return BenzSedan()
        if company == "Audi":
            return AudiSedan()
        return None
# This is a CarTypeFactory, which will return a Factory based on car type.
class CarTypeFactory:
    # Here we declare this method as static, to make it accessible by using CarTypeFactory class.
    # And this method will return Factory objects based on car type.
    @staticmethod
    def getCarType(type = None):
        if type == "SUV":
            return SUVFactory()
        if type == "Sedan":
            return SedanFactory()
        return None 
# Client Code 
cartype1 = CarTypeFactory.getCarType("SUV") # We create a "SUV" car
car1 = cartype1.getCar("RangeRover") # In "SUV" car type, we create a "RangeRover" car
car1.display() # Prints "This is a RangeRover SUV"
cartype2 = CarTypeFactory.getCarType("Sedan") # We create a "Sedan" car 
car2 = cartype2.getCar("Audi") # In "Sedan" car type, we create a "Audi" car 
car2.display() # Prints "This is a Audi Sedan"