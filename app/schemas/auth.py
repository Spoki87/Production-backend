import re
from pydantic import BaseModel, field_validator

class UserRegisterDTO(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: str) -> str:
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_regex, v):
            raise ValueError("Invalid email format")
        return v.lower()

class UserLoginDTO(BaseModel):
    email: str
    password: str