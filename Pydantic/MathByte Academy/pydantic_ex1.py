from pydantic import BaseModel, ValidationError, Field
from icecream import ic
from typing import Optional

class Person(BaseModel): 
    first_name : str = Field(strict=False)
    last_name : str = Field(strict=False)
    age: int = Field(strict=False)
    '''
    >> Below operator is not acceptable in python 3.9 it is introduced in python 3.10
    >> OFFICIAL DOC: required, can be None - same as str | None
    '''
    num: int | None
    # if we want to use Optional in v3.9 we need to do  
    '''
    OFFICIAL DOC: not required, can be None
    '''
    num2: Optional[int] = None


# it converts string into integer for integer fields but not converts integer into string for string fileds
p1 = Person(first_name="SHAHMEER", last_name="Khan", age="25", num="70")

ic(p1)

# Pydantic will cast/convert the data types on it's own if it's convertable

try:
    '''
    It Pydantic v2.5.4 converts string into integer and vice versa on Python 3.11 but in python 3.9 it 
    only converts string into integer but not viceversa.  
    
    '''
    p2 = Person(first_name="F",last_name="N",age="90", num=90 )
    ic(p2)
    ic(type(p2.age) )


except ValidationError as e:
    # Validation error can also display the error in JSON
    ic(e.json())

'''
NOTE: OFFICIAL DOC- Either .model_dump() or dict(user) will provide a dict of fields, but .model_dump() can take 
                    numerous other arguments. (Note that dict(user) will not recursively convert nested models into dicts, 
                    but .model_dump() will.)
'''