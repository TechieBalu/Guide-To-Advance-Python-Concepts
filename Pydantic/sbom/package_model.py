import sys
sys.path.append("..")
from pydantic import BaseModel,  field_validator, Field, model_validator
from spdx_tools.spdx.model import SpdxNoAssertion, SpdxNone
from typing import Optional
from license_expression import LicenseSymbol
from spdx_tools.common.spdx_licensing import spdx_licensing
import re
from cv_foss_bom_generator.exceptions.shared_exception import PackageFieldNone

class PackageModel(BaseModel):
    '''
    Model to validate Package
    
    '''
    name:str  = Field(strict=True)
    spdx_id:str 
    download_location:str ##pattern = (https?|ftp){1}:?//[A-Za-z\-._]+\.[A-Za-z_\-#/0-9=.]+
    version:str
    license_concluded : None | LicenseSymbol
    copyright_text:str 
    license_info_from_files: Optional[str] = None
    license_declared: Optional[str] = None
    license_comment: Optional[str] = None
    description: Optional[str] = None
    attribution_texts: Optional[str] = None
    primary_package_purpose: Optional[str] = None

    class Config:
        arbitrary_types_allowed=True

    @field_validator("download_location", mode='before')
    @classmethod
    def validate_download_location(cls,value):
        if value == None:
            value = "https://www.asml-default.com/" 
        return value
    

    @field_validator("license_concluded", mode='before')
    @classmethod
    def validate_license_concluded(cls,value): 
        pattern = r'[",!*/\\\s]'
        license = re.sub(pattern, '', value)
        license = spdx_licensing.parse(license)
        license = license.key 
        license = LicenseSymbol(license)
        
        return license

    
    @field_validator("copyright_text", mode='before')
    @classmethod
    def validate_copyright_text(cls,value:str):
        value_encode = value.encode("ascii", "ignore")
        value_decode = value_encode.decode()

        return value_decode
    
    @model_validator(mode='before')
    @classmethod
    def validator_all_fields(cls, data):
        none_pairs = [(key, value) for key, value in data.items() if value is None]

        if len(none_pairs) > 0:
            ex = PackageFieldNone(f"Value cannot be None for: '{none_pairs}' for Package: '{data.get('name')}'")
            raise ex
        
        return data 