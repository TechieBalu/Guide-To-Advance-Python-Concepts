# Python doesnot have builtin functionality of creating the abstract classes but we can do it using the "abc" module 
# we cannot create objects of abstract classes, rather we need to create an object of child class in which 
# methods of abstracted classes are overriddent

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def parameter(): pass

    @abstractmethod
    def area(): pass


class Square(Shape):
    