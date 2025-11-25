from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import settings


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="RAG-based FAQ service for SmartTask documentation",
    version="1.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=sorted(settings.BACKEND_CORS_ORIGINS),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Apply static files mount
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include the API router
# Versioned API (v1)
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    # Перенаправляем на статическую страницу index.html
    return RedirectResponse(url="/static/index.html")

