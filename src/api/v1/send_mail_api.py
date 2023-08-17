from fastapi import APIRouter, status
from fastapi_mail import ConnectionConfig, MessageSchema, MessageType, FastMail
from starlette.responses import JSONResponse

from schemas.mail_schema import EmailCreate
from core.config import app_settings

mail_router = APIRouter()


def set_conf(values: dict) -> ConnectionConfig:
    return ConnectionConfig(
        MAIL_USERNAME=values.get("username"),
        MAIL_PASSWORD=values.get("password"),
        MAIL_FROM=values.get("username"),
        MAIL_PORT=values.get("port"),
        MAIL_SERVER=values.get("server"),
        MAIL_STARTTLS=True,
        MAIL_SSL_TLS=False,
        USE_CREDENTIALS=True,
        VALIDATE_CERTS=True
    )


def is_valid_token(token: str) -> bool:
    return token == app_settings.secret_key


@mail_router.get("/")
async def index():
    return {"message": "The SendMil API"}


@mail_router.get("/ping")
async def ping():
    return {"message": "pong"}


@mail_router.post("/test")
async def test(values: EmailCreate):
    values = dict(values)
    if not is_valid_token(values.get("token")):
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content={"error": "wrong token"})
    return values


@mail_router.post("/send")
async def send_mail(values: EmailCreate) -> JSONResponse:
    values = dict(values)
    if not is_valid_token(values.get("token")):
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content={"error": "wrong token"})

    message = MessageSchema(
        subject=values.get("subject"),
        recipients=[values.get("emai_to")],
        body=values.get("body"),
        subtype=MessageType.html)
    fm = FastMail(set_conf(values))
    try:
        response = await fm.send_message(message)
    except Exception as err:
        return JSONResponse(status_code=status.HTTP_409_CONFLICT,
                            content={"error": err})

    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": "email has been sent",
                                 "response": response})
