
from ..schemas import logo
from fastapi import APIRouter, Request
router = APIRouter()

@router.get("/logoIcons", response_model=logo.LogoIconList)
async def get_logo_icons(request: Request):
    domain = str(request.base_url)
    icons = [
        {
            "name": "Flask",
            "src": f"{domain}static/images/svg/Flask.svg",
            "url": "https://flask.palletsprojects.com",
        },
        {
            "name": "fastapi",
            "src": f"{domain}static/images/svg/fastapi-1.svg",
            "url": "https://fastapi.tiangolo.com",
        },
        {
            "name": "tailwind",
            "src": f"{domain}static/images/svg/tailwindcss-mark.d52e9897.svg",
            "url": "https://tailwindcss.com",
        },
    ]
    return icons
