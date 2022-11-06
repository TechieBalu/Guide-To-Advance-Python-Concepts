'''
Generators: By using the yield keyword instead of return, we make the function as Generator, 
in other words, if we used yield keyword in the function, that function will be called Generator.  
Important: we use the next() object to call that particular generator again and again. 

For comprehensive explanation, read python-advance.doc file at github.

'''

def list_generator(l1): 
    for i in l1: 
        yield i


l1=[1,2,3,4]
a = list_generator(l1)
print(next(a))
print(next(a))
print(next(a))