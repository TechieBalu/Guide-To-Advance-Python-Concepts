import ctypes 



def fun(): 
    x = 10 
    print(x)
    id1 = id(x)
    del x
    # print(x)
    return id1

a = fun()
print(a)
print(id(a))
print(ctypes.cast(a,ctypes.py_object).value)


print("_____________________________________________________")

def fun2():
    x = 1000
    print(x)
    

x = 100
fun2()
print(x)

print("_____________________________________________________")


def outer_function():
    y = 20  # y is in the enclosing scope of inner_function

    def inner_function():
        x = y + 100
        print(x)

    inner_function()  # Prints 21
    print(y)

outer_function()



def outer_function():
    y = 20  # y is in the enclosing scope of inner_function

    def inner_function():
        print(y)

    inner_function()  # Prints 21
    print(y)

outer_function()