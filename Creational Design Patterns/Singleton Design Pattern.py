'''
Singleton Design Pattern: https://blog.algomaster.io/p/singleton-design-pattern
Singleton Pattern is a creational design pattern that guarantees a class has only one instance
and provides a global point of access to it.
It involves only one class which is responsible for instantiating itself, making sure it creates not more than one instance.
'''
 
# Lazy Evaluation
 
class Singleton:
    __instance = None # This is a class variable i.e. instance of our Singleton class which is private
    # We are using staticmethod here because, this should be accessible using our class.
    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton() # We create a Singleton object 
        return Singleton.__instance
    def __init__(self): # Our constructor
        # Before Executing we need to check whether an object/instance of this class is already
        # created or not. If it is already created we raise an Exception.
        # Else we create our instance and set it to Singleton instance
        if Singleton.__instance != None: 
            print("Singleton object already created")
        else:
            Singleton.__instance = self # Whenver a Singleton object gets created
 
# Client code 
obj1 = Singleton.getInstance() # As there is no instance created on this class 
obj2 = Singleton.getInstance() # This will return the same instance that is already created
 
# But most programmers create objects/instances in the below format rather than calling getInstance() static method.
# But as we are using __init__ constructor in python unlike Java, if the instance is already created
# it will raise an Exception as we have written above.
 
obj3 = Singleton()
print(obj3)
 
  
##########################################################################################################################################
 
# The problem with above code is that suppose the client code contains creation of two objects
# then when we try to create the second object, it will give us an exception that an instance is 
# already created. We do not want that, what we want is whether we can create as many objects as we
# want but they should point to the same single object that is created for the first time. So 
# this is easy to implement in Java but not in python. In python we use a special magic/dunder method called , 
# '__new__' which is basically used for operator overloading in python.
 
# Lazy Evaluation
 
class Singleton:
    __instance = None # This is a class variable i.e. instance of our Singleton class which is private
    # We are using staticmethod here because, this should be accessible using our class.
    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton() # We create a Singleton object 
        return Singleton.__instance
    # __init__ and __new__ are called whenever objects are created on this class. 
    # I am not writing more about this '__new__' method, you can check for yourself
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance
 
# Client code 
obj1 = Singleton.getInstance() # As there is no instance created on this class 
obj2 = Singleton.getInstance() # This will give the same instance that is already created
obj3 = Singleton() # This will also give the same instance that is created unlike our previous code
obj4 = Singleton() # This will also give the same instance that is created unlike our previous code
print(obj1)
print(obj2)
print(obj3)
print(obj4)
obj1.x = 10 # 
print(obj4.x) # It will print 10 as all the objects point to same single instance of our class
 
#######################################################################################################################################
 
# Ok so the above code is fine. But what if there multiple threads creating the objects so how do you make this thread-safe?
 
# Thread - Safe Singleton
 
import threading
 
class Singleton:
    __instance = None 
    __lock = threading.Lock() 
    # We set a class variable named "__lock" to our threading.Lock 
    # which will be used for locking as specific resource/block of code
    def __new__(cls):
        # So whenever multiple threads come in, a thread sets the lock to the resource
        # and creates the instance if the instance is not already created and releases the lock 
        # after its done. So hence thread-safety is achieved.
        # This acts same like "synchronized" keyword in Java, i.e. it locks the resource
        # or block of code when a thread comes in and releases that lock after its done.
        with cls.__lock: 
            if cls.__instance == None:
                cls.__instance = super(Singleton, cls).__new__(cls)
            return cls.__instance
 
s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)
 
##################################################################################################################
 
# The problem with the above code is even though thread safety is achieved.
# For each thread we trying to lock the resource/block of code.
# And locking is an expensive operation, and locking the resource for each thread 
# is not very efficient. So before locking we do check. This is called Double Locking.
# And this is the most used method for creating Singleton class instance in the industry.
 
# Double - Locking
 
import threading
 
class Singleton:
    __instance = None 
    __lock = threading.Lock() 
    def __new__(cls):
        # So we do a double check if an instance is already created or not. 
        # If it is not created then only we set the lock
        if cls.__instance == None:
            with cls.__lock: 
                if cls.__instance == None:
                    cls.__instance = super(Singleton, cls).__new__(cls)
        
        return cls.__instance
 
s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)
