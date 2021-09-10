from pydantic import BaseModel

class Employee(BaseModel):
    fname: str
    mname: str =None
    lname: str
    email: str
    department_id: int

    class Config:
        orm_mode=True

class Department(BaseModel):
    name: str

    class Config:
        orm_mode=True