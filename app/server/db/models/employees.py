from datetime import datetime

from beanie import Document
from pydantic import EmailStr


class Employees(Document):
    name: str
    email: EmailStr
    age: int
    company: str
    join_date: datetime
    job_title: str
    gender: str
    salary: int

    class Settings:
        name = "employees"

    class Config:
        schema_extra = {
            "example": {
                "name": "Judah Melton",
                "email": "mauris@interdum.net",
                "age": 69,
                "company": "Twitter",
                "join_date": "2003-11-29T07:50:38-08:00",
                "job_title": "designer",
                "gender": "female",
                "salary": 4575,
            }
        }
