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
    # num: int | None
    # if we want to use Optional in v3.9 or below 3.10 we need to do  
    '''
    OFFICIAL DOC: not required, can be None
    '''
    num2: Optional[int] = None


# it converts string into integer for integer fields but not converts integer into string for string fileds
p1 = Person(first_name="SHAHMEER", last_name="Khan", age="25")

ic(p1)

# Pydantic will cast/convert the data types on it's own if it's convertable

try:
    '''
    It Pydantic v2.5.4 converts string into integer and vice versa on Python 3.11 but in python 3.9 it 
    only converts string into integer but not viceversa.  
    
    '''
    p2 = Person(first_name="F",last_name="N",age="90", num=90 )
    ic(p2)
    ic(type(p2) )


except ValidationError as e:
    # Validation error can also display the error in JSON
    ic(e.json())

'''
NOTE: OFFICIAL DOC- Either .model_dump() or dict(user) will provide a dict of fields, but .model_dump() can take 
                    numerous other arguments. (Note that dict(user) will not recursively convert nested models into dicts, 
                    but .model_dump() will.)
'''

# * Transforming Person class object into python dict 
print("\nTransforming Person class object into python dict ")
p1_to_dict = p1.model_dump()
ic(type(p1_to_dict), p1_to_dict)

# * Transforming Person class object into json directly
print("\nTransforming Person class object into json directly")
p1_to_json = p1.model_dump_json()
ic(type(p1_to_json), p1_to_json)

# * Excluding some fields, while using model_dump 
print("\nExcluding some fields, while using model_dump ")
p1_to_dict = p1.model_dump(exclude=["num2"])
ic(type(p1_to_dict), p1_to_dict)


# * Excluding some fields, while using model_dump_json 
print("\nExcluding some fields, while using model_dump ")
p1_to_dict = p1.model_dump_json(exclude={"age"}) # In exlude, we can use lists, tuples and sets of values
ic(type(p1_to_dict), p1_to_dict)
