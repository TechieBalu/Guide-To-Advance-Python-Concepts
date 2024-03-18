import sys
sys.path.append("..")
from pydantic import BaseModel,  field_validator, StringConstraints, DirectoryPath, FilePath
from cv_foss_bom_generator.exceptions.shared_exception import InputExceptions
from typing_extensions import Annotated
import pathlib
import datetime

class InputModel(BaseModel):
    '''
    Model to validate Document Name and File 
    
    '''
    name:str  = Annotated[str, StringConstraints(strip_whitespace=True)] 
    file_path:str 
    output_path: DirectoryPath

    @field_validator("file_path", mode='after')
    @classmethod
    def validate_file_path(cls,value:str):
        allowed_extensions = ('.xlsx','.csv')
        ext = pathlib.Path(value).suffix 
        if ext not in allowed_extensions:
            raise InputExceptions("File Should be in {} Format".format(allowed_extensions))
        return value

    @field_validator("name", mode='before')
    @classmethod
    def validate_name(cls,value:str):
        if value is None or value.strip() == "": 
            raise InputExceptions()
        value = value + " " + datetime.datetime.now().strftime(r"%d_%m_%Y %H_%M_%S")
        return value 
    