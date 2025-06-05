
from ..schemas import logo
from fastapi import APIRouter, Request
router = APIRouter()

@router.get("/logoIcons", response_model=logo.LogoIconList)
async def get_logo_icons(request: Request):
    domain = str(request.base_url)
    icons = [
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
        {
            "name": "vercel",
            "src": f"{domain}static/images/svg/vercel-icon-svgrepo-com.svg",
            "url": "https://vercel.com/",
        }
    ]
    return icons
