from fastapi import APIRouter

from api.v1.send_mail_api import mail_router

api_router = APIRouter()
api_router.include_router(mail_router, tags=["Mail"])
# api_router.include_router(mail_router, prefix="/mails", tags=["Mail"])
