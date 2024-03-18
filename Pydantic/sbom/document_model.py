import sys
sys.path.append("..")
from pydantic import BaseModel, StringConstraints, field_validator
from typing import Optional, List
from spdx_tools.spdx.model import Actor, ActorType
from datetime import datetime
from typing_extensions import Annotated
from cv_foss_bom_generator.exceptions.shared_exception import DocumentFieldNone


class DocumentModel(BaseModel):
    '''
    Model to validate document fields
    '''
    spdx_version:str = "SPDX-2.3"
    spdx_id:str = "SPDXRef-DOCUMENT"
    name: Annotated[str, StringConstraints(min_length=3, strip_whitespace=True)] 
    data_license:str = "CC0-1.0" #By Default it's CC0-1.0
    document_namespace:Annotated[str, StringConstraints(strip_whitespace=True)] = "https://www.asml.com/" #pattern = (https?|ftp){1}:?//[A-Za-z\-._]+\.[A-Za-z_\-#/0-9=.]+
    creators:List = [Actor(ActorType.PERSON, "ASML Netherlands B.V.", "dl-3rdpartysw-core@asml.com")] #Takes list of objects of Actor
    created:datetime = datetime.utcnow()

    @field_validator("name", mode="before")
    @classmethod 
    def validate_document_name(cls,name): 

        if name == None:
            raise DocumentFieldNone("Name of Document cannot be None")
        return name