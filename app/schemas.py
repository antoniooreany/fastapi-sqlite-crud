from pydantic import BaseModel, ConfigDict, Field

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)


class ItemUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=100)
    price: float | None = Field(None, gt=0)


class ItemResponse(BaseModel):
    id: int
    name: str
    price: float

    model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8)

class UserResponse(BaseModel):
    id: int
    username: str
    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
