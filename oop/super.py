class Parent:
    def __init__(self) -> None:
        print("This is parent class")

class Child(Parent):
    def __init__(self) -> None:
        super().__init__()
        print("This is CHILD")


ch = Child()