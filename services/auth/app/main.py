import logging

from fastapi import FastAPI

from app.api.api_v1 import api
from app.db import init_db
from app.auth_grpc import start_grpc_server_in_thread


def create_application() -> FastAPI:
    application = FastAPI(
        openapi_url="/auth/openapi.json",
        docs_url="/auth/docs")
    application.include_router(
        api.router,
        tags=["auth"],
    )
    return application


app = create_application()
log = logging.getLogger("uvicorn")


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)
    start_grpc_server_in_thread()


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
