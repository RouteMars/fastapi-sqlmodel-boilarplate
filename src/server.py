from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from loguru import logger

from src.controller.user_controller import router
from src.database.database import init_db
from src.util.log_config import setup_logging

setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()  # 앱 시작 시 DB 초기화
    logger.info("🚀 FastAPI 앱 시작")
    yield
    logger.info("🛑 FastAPI 앱 종료")


app = FastAPI(lifespan=lifespan)


@app.middleware("http")
async def interceptor_middleware(request: Request, call_next):
    scheme = request.url.scheme  # http 또는 https
    logger.info(f"{scheme.upper()} Request: {request.method} {request.url.path}")
    # logger.info("Before request")
    response = await call_next(request)
    # logger.info("After response")
    return response


def create_server():
    app.include_router(router)
    return app
