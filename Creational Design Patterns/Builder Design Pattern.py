'''
 
Builder Design Pattern :
 
Builder is a creational design pattern that lets you construct complex objects step by step.
The pattern allows you to produce different types and representations of an object using the same construction code.
 
Problems that arise without using Builder Design Pattern:
 
--- Imagine a complex object that requires laborious, step-by-step initialization of many fields and nested objects.
Such initialization code is usually buried inside a monstrous constructor with lots of parameters. Or even worse:
scattered all over the client code. 
For example, let’s think about how to create a House object. To build a simple house, you need to construct four
walls and a floor, install a door, fit a pair of windows, and build a roof. But what if you want a bigger, brighter
house, with a backyard and other goodies (like a heating system, plumbing, and electrical wiring)?
The simplest solution is to extend the base House class and create a set of subclasses to cover all combinations of 
the parameters. But eventually you’ll end up with a considerable number of subclasses. Any new parameter, such as the 
porch style, will require growing this hierarchy even more.
 
--- There’s another approach that doesn’t involve breeding subclasses. You can create a giant constructor right in
the base House class with all possible parameters that control the house object. While this approach indeed eliminates 
the need for subclasses, it creates another problem. In most cases most of the parameters will be unused, making the 
constructor calls pretty ugly. For instance, only a fraction of houses have swimming pools, so the parameters related
to swimming pools will be useless nine times out of ten.
 
Solution to these problems is Builder Design Pattern:
 
The Builder pattern suggests that you extract the object construction code out of its own class and move it to
separate objects called builders.
 
The pattern organizes object construction into a set of steps. To create an object, you execute a series of these 
steps on a builder object. The important part is that you don’t need to call all of the steps. You can call only 
those steps that are necessary for producing a particular configuration of an object.
 
'''
 
from abc import ABC, abstractmethod
 
# This is a House class, which takes a builder object, and initalizes all its parameters 
# equal to builder parameters
class House:
    def __init__(self, builder):
        self.stories = builder.stories 
        self.door_type = builder.door_type
        self.roof_type = builder.roof_type
# This is a HouseBuilder class, which is responsible to build on the builder object i.e. itself
class HouseBuilder:
    # Initially all the parameters of this builder object are set to None.
    def __init__(self):
        self.stories = None 
        self.door_type = None 
        self.roof_type = None 
    # This method will set our stories value to our builder object and return our builder object
    def setStories(self, stories):
        self.stories = stories 
        return self 
    # This method will set our door type value to our builder object and return our builder object 
    def setDoorType(self, doorType):
        self.door_type = doorType 
        return self 
    # This method will set our roof type value to our builder object and return our builder object 
    def setRoofType(self, roofType):
        self.roof_type = roofType 
        return self 
    # And finally our build function which create and return a new House object based on our builder object
    # that we pass as the parameter
    def build(self):
        return House(self)
    
# Client Code 
one_story_builder = HouseBuilder() # We first create a house builder object
# Then we set our stories to 2 on this house builder object which will be step 1 and store the builder object 
# which will be returned in one_story_build_step_1
one_story_build_step_1 = one_story_builder.setStories(2) 
# Then we set our door type to "Black" on this house builder object which will be step 2 and store the builder 
# object which will be returned in one_story_build_step_2
one_story_build_step_2 = one_story_build_step_1.setDoorType("Black")
# Then we set our roof type to "Pointy" on this house builder object which will be step 3 and store the builder 
# object which will be returned in our one_story_step_3
one_story_build_step_3 = one_story_build_step_2.setRoofType("Pointy")
# Finally we build a house by calling our build() method of our one_story_build_step_3 builder object, which 
# will return a House object with all the parameters equal to our one_story_build_step_3 builder object.
one_story_house = one_story_build_step_3.build() # This will give a House object with all parameter values equal to our builder object
print(isinstance(one_story_house, House))# And remember this is a House object not a House builder object you can check with 'isinstance()' method
# The above line will print True.
 
'''
And as you can see in the client there are several build steps involved to build a 
particular house. But if there are specific steps to build a particular object using 
a builder i.e. there are specific steps to build One story house and specific steps
to build two story house, then we can have a specific builder with that steps assigned 
to it. This way we can have various builders for building different complicated objects 
and we can use a Director which will help us managing those builders.
 
'''
 
 
from abc import ABC, abstractmethod
 
# This is a House class, which takes a builder object, and initalizes all its parameters 
# equal to builder parameters
class House:
    def __init__(self, builder):
        self.stories = builder.stories 
        self.door_type = builder.door_type
        self.roof_type = builder.roof_type
# This is a HouseBuilder class, which is responsible to build on the builder object i.e. itself
class HouseBuilder:
    # Initially all the parameters of this builder object are set to None.
    def __init__(self):
        self.stories = None 
        self.door_type = None 
        self.roof_type = None 
    # This method will set our stories value to our builder object and return our builder object
    def setStories(self, stories):
        self.stories = stories 
        return self 
    # This method will set our door type value to our builder object and return our builder object 
    def setDoorType(self, doorType):
        self.door_type = doorType 
        return self 
    # This method will set our roof type value to our builder object and return our builder object 
    def setRoofType(self, roofType):
        self.roof_type = roofType 
        return self 
    # And finally our build function which create and return a new House object based on our builder object
    # that we pass as the parameter
    def build(self):
        return House(self)

# Director Class which will manage our different builders, it will take a builder object while Initializing,
# And using this builder object it build our house and return a House object.
class Director:
    # Initializing our builder object
    def __init__(self, builder):
        self.builder = builder 
    # Function to build one story house, this will build our one story House
    # step by step and return our House object
    def build_one_story_house(self):
        return self.builder.setStories(2).setDoorType("Black").setRoofType("Pointy").build()
    # Function to build two story house, this will build our two story House 
    # step by step and return our House object
    def build_two_story_house(self):
        return self.builder.setStories(3).setDoorType("White").setRoofType("Flat").build()

 
# Client code 
builder_obj = HouseBuilder() # First we create a builder object which will responsible for building our House  
director_obj = Director(builder_obj) # Then we have a director object, which will take our builder object and 
# and using this director object we can build one story or two story houses.
house1 = director_obj.build_one_story_house() # So for building a one story house we can simply call the 
# "build_one_story_house()" method in our Director class using our director object.
print(house1.stories) # Prints "2"
print(house1.door_type) # Prints "Black"
print(house1.roof_type) # Prints "Pointy"
print(isinstance(house1, House)) # And remember this is a House object not a House builder object you can check with 'isinstance()' method
# The above line will print True.
house2 = director_obj.build_two_story_house() # And for building a two story house we can simply call the 
# "build_two_story_house()" method in our Director class using our director object
print(house2.stories) # Prints "3"
print(house2.door_type) # Prints "White"
print(house2.roof_type) # Prints "Flat"
print(isinstance(house2, House)) # And remember this is a House object not a House builder object you can check with 'isinstance()' method
# The above line will print True.
 
'''
So this way Director is really helpful in managing specific builder which are responsible for building specific
complicated objects. Use of this Director is not mandatory.
 
Many people get confused between the Builder Design Pattern and Decorator Pattern as they look similar.
The difference between builder Design pattern and decorator design pattern are:
 
 
                     Builder Design Pattern           |        Decorator Design Pattern
              ----------------------------------------|-----------------------------------------                                  
                                                      |
            --- Creational Design Pattern.            | --- Structural Design Pattern.
                                                      |
            --- And the major difference is that the  | --- Decorator can handle dynamic creation 
                builder Design pattern cannot handle  |     of objects.
                dynamic creation of objects i.e.      |
                we cannot build a new object with new |
                specifications that we do not have a  |
                paritcular builder to build that      |
                object.                               |
                                                      |
 
'''