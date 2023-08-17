import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import base_api
from core.config import app_settings

app = FastAPI(
    title=app_settings.project_name,
    docs_url="/api/v1/docs",
    openapi_url="/api/v1/openapi.json",
    default_response_class=ORJSONResponse,
)

app.include_router(base_api.api_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=app_settings.project_host,
        port=app_settings.project_port,
        reload=True,
    )
