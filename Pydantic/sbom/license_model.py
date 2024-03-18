from pydantic import BaseModel, StringConstraints, field_validator
from license_expression import get_spdx_licensing
from typing_extensions import Annotated
from typing import Tuple
import re



class LicenseModel(BaseModel):
    '''
    Model to validate the license - either SPDX or non-SPDX
    '''
    license_concluded: Annotated[str, StringConstraints(strip_whitespace=True)] | Tuple[bool,str] | None    

    @field_validator("license_concluded", mode='before')
    @classmethod
    def license_validator(cls,value):
        def license_cleaner(value):
            '''      
            replace all spaces with "-"
            '''
            refined_license = re.sub(r'\s+', '-', value)
            refined_license = re.sub(r'[^a-zA-Z0-9-.]', '', refined_license)
            return refined_license
        
        ret = None
        if value:
            try:
                licensing = get_spdx_licensing()
                result = licensing.validate(value)
                if len(result.invalid_symbols) > 0:
                    refined_license = license_cleaner(str(result.original_expression).strip())
                    ret = False, "LicenseRef-"+refined_license
                else:
                    ret = value 
            except:
                refined_license= license_cleaner(value.strip())
                ret = False, "LicenseRef-"+refined_license
                
        return ret