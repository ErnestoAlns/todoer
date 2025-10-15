from pydantic import BaseModel, Field, ConfigDict
from datetime import date 

class TaskRegister(BaseModel):
    title: str = Field(min_length=8, max_length=70)
    desc: str = Field(min_length=10)

    model_config = ConfigDict(from_attributes=True)

class TaskModel(BaseModel):
    create_by: int
    daydate: date
    titile: str
    desc: str

    model_config = ConfigDict(from_attributes=True)
    

