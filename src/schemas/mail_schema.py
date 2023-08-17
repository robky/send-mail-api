from pydantic import BaseModel, EmailStr


class EmailBase(BaseModel):
    emai_to: EmailStr
    subject: str
    body: str


class EmailCreate(EmailBase):
    token: str
    username: EmailStr
    password: str
    port: int
    server: str


class EmailSchema(EmailBase):
    pass
