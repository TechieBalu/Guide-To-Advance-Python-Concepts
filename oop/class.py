class Car:

    # This is exactly not the constructor but very close to the constructor, we call it a constructor because it is the first method that is called when 
    # we create the object of a class. (Explre difference between the constructor and __init__ method of python class)
    
    def __init__(self) -> None:
        pass 


ford = Car()
honda = Car()
audi = Car()

ford.speed = 200
honda.speed = 200
audi.speed = 200

ford.color = 'red'
honda.color = 'blue'
audi.color = 'green'

print(audi.speed, audi.color)

