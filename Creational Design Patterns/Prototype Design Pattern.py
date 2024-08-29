'''
Prototype Design Pattern: https://refactoring.guru/design-patterns/prototype
 
Prototype is a creational design pattern that lets you copy existing objects without 
making your code dependent on their classes.
 
Problems without Prototype:
 
1) Say you have an object, and you want to create an exact copy of it. How would you do it? 
First, you have to create a new object of the same class. Then you have to go through all 
the fields of the original object and copy their values over to the new object.
Nice! But there’s a catch. Not all objects can be copied that way because some of the object’s
fields may be private and not visible from outside of the object itself.
 
2) There’s one more problem with the direct approach. Since you have to know the object’s
class to create a duplicate, your code becomes dependent on that class. Basically this 
means that we have to depend on the Client to create the clone object.
 
3) If the extra dependency doesn’t scare you, there’s another catch. Sometimes you only 
know the interface that the object follows, but not its concrete class, when, for example, 
a parameter in a method accepts any objects that follow some interface.
 
'''
 
# So the below example is cloning objects without using Prototype Design Pattern.
 
# Original Object class
class Student:
    def __init__(self, name = None, age = None, rollNumber = None):
        self.name = name 
        self.age = age 
        self.__rollNumber = rollNumber # Private Variable

# Client code 
obj = Student("John", 24, 1)
cloneObj = Student()
 
# Here client is responsible for copying all the attributes of 
# orignal object to the cloned object, which shouldn't be the case.
cloneObj.name = obj.name 
cloneObj.age = obj.age 
cloneObj.__rollNumber = obj.__rollNumber 
# The last line will give you an error because you can't access private variables outside the class.
# You can use setter and getter methods in Student class to set and get the private variables values.
 
'''
 
The Prototype pattern delegates the cloning process to the actual objects that are being cloned. 
The pattern declares a common interface for all objects that support cloning. This interface lets 
you clone an object without coupling your code to the class of that object. Usually, such an interface
contains just a single clone method.
 
The implementation of the clone method is very similar in all classes. The method creates an object of 
the current class and carries over all of the field values of the old object into the new one. 
You can even copy private fields because most programming languages let objects access private fields 
of other objects that belong to the same class.
 
An object that supports cloning is called a prototype. When your objects have dozens of fields and hundreds 
of possible configurations, cloning them might serve as an alternative to subclassing.
 
'''
 
# Cloning using Prototype Design pattern
 
from abc import ABC, abstractmethod
 
# Prototype Interface
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass
 
# Original Object class
class Student(Prototype):
    def __init__(self, name = None, age = None, rollNumber = None):
        self.name = name 
        self.age = age 
        self.__rollNumber = rollNumber # Private Variable

    # This clone() method will return new Student object with all the attributes/fields same as 
    # old object i.e. it carries over all of the field values of the old object into the new one.
    def clone(self):
        return Student(self.name, self.age, self.__rollNumber)
    # Getter method to get the value of private variable self.__rollNumber (This is used for checking
    # if our original object value matches the clone objects value)
    def getRollNumber(self):
        return self.__rollNumber

# Client Code
obj = Student("John", 23, 1) # Create a Student object.
print(obj) # Original object
 
# Now you can just create a clone by just calling the clone() method using the old object, 
# which will return a clone Object with all the attributes/field values same as the previous old object.
clone1 = obj.clone() 
print(clone1) # Clone object of Original object
clone2 = obj.clone() # Another clone object of Orignal object
 
# We can also intern create clones using our previous clone objects.
clone3 = clone1.clone() # Clone object of our clone1 object
print(clone2)
print(clone3)
 
# Even private variables from old to new objects gets copied, you can check the
# private variables by using the getter method that is present in our Student class
print(clone3.getRollNumber())