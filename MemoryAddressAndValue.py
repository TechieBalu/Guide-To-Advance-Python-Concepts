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

