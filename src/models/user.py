from pydantic import BaseModel, ConfigDict, Field

class UserRegister(BaseModel):
    username: str = Field(min_length=4, max_length=50)
    password: str = Field(min_length=4, max_length=100)

    model_config = ConfigDict(from_attributes=True)

class UserModel(BaseModel):
    id: int
    name: str
    password: str

    model_config = ConfigDict(from_attributes=True)

