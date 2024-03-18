from pydantic import BaseModel, FilePath, StringConstraints, field_validator, EmailStr, DirectoryPath
from typing_extensions import Annotated
import pathlib

class PDFModel(BaseModel):
    '''
    Validate PDF generation parameters
    '''
    project_name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=3, max_length=50)] 
    version : Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=10)] 
    file_path: FilePath
    copy_rights : Annotated[str, StringConstraints(strip_whitespace=True, max_length=100)] | None
    output_document_name:  Annotated[str, StringConstraints(strip_whitespace=True, max_length=100, min_length=3)]
    dest_path: DirectoryPath
    title: Annotated[str, StringConstraints(strip_whitespace=True, max_length=100 )]  
    author: Annotated[str, StringConstraints(strip_whitespace=True, max_length=100)]  
    ci_name: Annotated[str, StringConstraints(strip_whitespace=True, max_length=100, min_length=3)]  | None
    ci_address: Annotated[str, StringConstraints(strip_whitespace=True, max_length=100, min_length=3)]  | None
    ci_office: Annotated[str, StringConstraints(strip_whitespace=True, max_length=100, min_length=3)] | None
    ci_phone: Annotated[str, StringConstraints(strip_whitespace=True, max_length=100, min_length=3)] | None
    ci_email: EmailStr

    @field_validator("output_document_name", mode='after')
    @classmethod
    def validate_output_document_name(cls, value:str):

        if not value.isalnum():
            raise ValueError("Output should contain only alphanumeric characters")
        
        return value
    

    @field_validator("file_path", mode='after')
    @classmethod
    def validate_file_path(cls, value):

        if pathlib.Path(value).suffix != '.json':
            raise ValueError("Incorrect Format: File should be in SPDX Json format")
        
        return value