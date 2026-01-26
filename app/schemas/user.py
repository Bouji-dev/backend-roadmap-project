from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    age: int = Field(..., gt=0, lt=120)



class UserResponse(BaseModel):
    id: int
    email: EmailStr
    age: int
    