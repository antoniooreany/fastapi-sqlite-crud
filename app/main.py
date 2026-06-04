import uuid
import time
import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.routers import items as items_router, auth as auth_router
from app.logging_utils import setup_logging
from app.config import settings

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.app_title,
    description="Simple REST API with FastAPI, SQLite and a tiny frontend",
    version=settings.app_version,
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    request_id = str(uuid.uuid4())
    # This allows us to use request_id in our logs
    # We use a context var or just pass it in 'extra' when logging
    # For simplicity here, we'll attach it to the request state
    request.state.request_id = request_id
    
    start_time = time.time()
    
    # We can also add it to the logger's extra context via a custom filter or adapter
    # but for FastAPI, we can log the start and end of request with the ID
    logger.info(f"Request started: {request.method} {request.url.path}", extra={"request_id": request_id})
    
    response = await call_next(request)
    
    process_time = time.time() - start_time
    response.headers["X-Request-ID"] = request_id
    response.headers["X-Process-Time"] = str(process_time)
    
    logger.info(
        f"Request finished: {request.method} {request.url.path} - Status: {response.status_code}", 
        extra={"request_id": request_id, "process_time": process_time}
    )
    
    return response

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items_router.router)
app.include_router(auth_router.router)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_index():
    return FileResponse("static/index.html")
