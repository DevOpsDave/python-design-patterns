#!/usr/bin/env python3
"""
What does it do?
Create a method to create objects.

Why would you use it?
You can pass the factory methods arguments that are used for more extensive object creation.
Note how make accepts type argument.
"""

class CarFactory(object):
    def make(type):
        if type == "racecar":
            return RaceCar()
        elif type == "van":
            return Van()
        elif type == "bus":
            return Bus()
    
    make = staticmethod(make)

class RaceCar:
    type_name = "RaceCar"
    wheels = 4

class Bus:
    type_name = "Bus"
    wheels = 4

class Van:
    type_name = "Van"  # TODO: how do I reflect the class name here?
    wheels = 4

obj1 = CarFactory.make("racecar")
obj2 = CarFactory.make("van")

print(obj1.type_name)
print(obj2.type_name)