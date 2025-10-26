from mysql.connector import Timestamp
from pydantic import BaseModel, Field, ConfigDict
from datetime import date 

class TaskRegister(BaseModel):
    created_by: int
    titile: str = Field(min_length=4, max_length=70)
    descTask: str = Field(min_length=10)
    state: bool

    model_config = ConfigDict(from_attributes=True)

class TaskModel(BaseModel):
    id: int
    created_by: int
    daydate: Timestamp
    titile: str
    descTask: str
    state: bool

    model_config = ConfigDict(from_attributes=True)
    

