import logging

from fastapi import FastAPI

from app.api.api_v1 import api


def create_application() -> FastAPI:
    application = FastAPI(
        openapi_url="/blockchain/openapi.json",
        docs_url="/blockchain/docs")
    application.include_router(
        api.router,
        tags=["blockchain"],
    )
    return application


app = create_application()
log = logging.getLogger("uvicorn")


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
