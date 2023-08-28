class A:

    cool = 50
    def __init__(self, a_name):
        self.a_name = a_name

    
    def pr():
        print("IM A CLASS")
   
# Intermediate class
class B(A):
    def __init__(self, b_name, a_name):
       self.b_name = b_name
       # invoke constructor of class A
       A.__init__(self, a_name)
    
    def pr():
        print("IM B CLASS")
       

# Child class
class C(B):
    def __init__(self,c_name, b_name, a_name):
        self.c_name = c_name
        # print(super)
        # super().__init__(self, b_name, a_name)

       # invoke constructor of class B
        B.__init__(self, b_name, a_name)
    
    
    def pr():
        print("IM C CLASS")
       
    def display_names(self):
       print("A name : ", self.a_name)
       print("B name : ", self.b_name)
       print("C name : ", self.c_name)


class D(C,B):
    def __init__():
        # super().__init__(b_name, a_name)
        pass

# class A2(A):
#     def __init__(self, a_name):
#         super().__init__(a_name)

#  Driver code
obj1 = C('child', 'intermediate', 'parent')
print(obj1.a_name)
print(obj1.cool)

obj1.display_names()

print(A.__mro__)
print(B.__mro__)
print(C.__mro__)
