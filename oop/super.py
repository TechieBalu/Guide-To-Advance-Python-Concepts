class Parent:
    def __init__(self) -> None:
        print("This is parent class")


class Parent2:
    def __init__(self) -> None:
        print("This is parent2 class")

class Child(Parent, Parent2):
    def __init__(self) -> None:
        # super function is builtin function that return the proxy object that allows you to refer to parent class
        super().__init__()
        print("This is CHILD")


ch = Child()
# method resolution order 
# this is the method in which order that methods are calling inside child class 
# RULES: method inside sub class will be called first, after that method in base class will be called
# every class is finally inherited from the python object class, so that's why we see "class object" in results of __mro__
print(Child.__mro__)