from pydantic import Field,BaseModel;


class MovieRequest(BaseModel):
    name: str = Field(min_length=4,max_length=20);
    description: str = Field(min_length=4,max_length=20);
    categoryId: int = Field(ge=1);
    
class MovieUpdateRequest(BaseModel):
    name: str = Field(min_length=4,max_length=20);
    description: str = Field(min_length=4,max_length=20);