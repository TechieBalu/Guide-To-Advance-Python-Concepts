from pydantic import BaseModel, ValidationError, Field
from icecream import ic

class Person(BaseModel): 
    first_name : str = Field(strict=False)
    last_name : str = Field(strict=False)
    age : int = Field(strict=False)

p1 = Person(first_name="Shahmeer", last_name="Khan", age="25")

ic(p1)

# Pydantic will cast/convert the data types on it's own if it's convertable

try:
    p2 = Person(first_name="100",last_name="200",age="90")
    ic(p2.age)
    ic(type(p2.age) )


except ValidationError as e:
    print(e)