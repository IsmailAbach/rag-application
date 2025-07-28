from pydantic import BaseModel ,Field , validator
from typing import Optional
from bson.objectid import ObjectId

class Project(BaseModel) :
    _id : Optional[ObjectId]
    project_id : str = Field(..., min_length = 1)

    @validator('project_id')
    def validate_porject_id(cls,value) : 
        if not value.isalnum() :
            raise ValueError('Project Id must be alphanumeric')
        return value
    
    class config:
        arbitrary_types_allowed = True
