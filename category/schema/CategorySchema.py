from pydantic import BaseModel,Field;

class CategoryRequest(BaseModel):
    name: str = Field(max_length=20,min_length=4);
    description: str = Field(max_length=20,min_length=4);