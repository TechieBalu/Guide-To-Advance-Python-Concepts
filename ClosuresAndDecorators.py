import ctypes

def welcome():
    return "Hello World!"


wel = welcome()
# del welcome
print(id(welcome))
print(welcome)
print(id(wel))
# welcomeID = id(welcome)
welID = id(wel)
print(id(welID))
# print(ctypes.cast(id(welcome),ctypes.py_object).value)
print(ctypes.cast(id(wel),ctypes.py_object).value)


def deco(func):
    print("We are bad")
    x = 10
    func(x)
    return 7

@deco 
def myfunc(x):
    z = x+30
    print(z)
    print("We are GOOD")


myfunc