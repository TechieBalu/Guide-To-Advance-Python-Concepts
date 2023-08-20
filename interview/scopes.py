import ctypes 
def fun(): 
    x = 10 
    id1 = id(x)
    del x
    # print(x)
    return id1

a = fun()
print(a)
print(id(a))
print(ctypes.cast(a,ctypes.py_object).value)