from pydantic import BaseModel, ValidationError, Field
from icecream import ic

class Person(BaseModel): 
    first_name : str = Field(strict=False)
    last_name : str = Field(strict=False)
    age : int = Field(strict=False)
    # Below operator is not acceptable in python 3.9 it is introduced in python 3.10
    # num : int | None

p1 = Person(first_name="Shahmeer", last_name="Khan", age="25")

ic(p1)

# Pydantic will cast/convert the data types on it's own if it's convertable

try:
    # It v2.5.4 converts string into integer but not vice verse 
    p2 = Person(first_name="100",last_name=200,age="90")
    ic(p2.age)
    ic(type(p2.age) )


except ValidationError as e:
    # Validation error can also display the error in JSON
    ic(e.json())