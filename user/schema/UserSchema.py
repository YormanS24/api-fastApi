from pydantic import BaseModel,Field;

class UserRequest(BaseModel):
    name: str = Field(alias="user_name",min_length=4,max_length=20);
    password: str = Field(min_length=4,max_length=20);