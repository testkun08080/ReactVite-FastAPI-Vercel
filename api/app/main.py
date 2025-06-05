from fastapi import FastAPI, Request
from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

import os
from .core.config import Settings
from .api.logo import router as logo
from functools import lru_cache

settings = Settings()

# Create FastAPI app instance with settings
app = FastAPI(title=settings.project_name,
              description=settings.project_description,
              version=settings.version,
              root_path=settings.root_path)


# Add templates and static files
dirPath = os.path.dirname(os.path.realpath(__file__))
app.mount(
    "/static", StaticFiles(directory=os.path.join(dirPath, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(dirPath, "templates"))


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add router for logo api
app.include_router(logo, prefix="/logo")

@lru_cache
def get_settings():
    return Settings()

# Custom 404 handler
@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        # Rendering a custom 404 page
        return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    return HTMLResponse(content=str(exc.detail), status_code=exc.status_code)


# Root
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
