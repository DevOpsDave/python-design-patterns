#!/usr/bin/env python3

import queue

class Car:
    def __init__(self, name):
        self.name = name

    def showName(self):
        print(self.name)

obj1 = Car("volvo")
obj2 = Car("bmw")
obj3 = Car("chrysler")

q = queue.Queue()
q.put(obj1)
q.put(obj2)
q.put(obj3)

while not q.empty():
    obj = q.get()
    obj.showName()