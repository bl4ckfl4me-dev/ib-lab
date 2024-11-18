from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import APIRouter, Request
from cript import decode_access_token
from db.crud import get_user_by_nickname


router = APIRouter()
templates = Jinja2Templates(directory='src/templates')


@router.get("/login")
async def get_login_page(request: Request):
    return templates.TemplateResponse(name='login.html', context={'request': request})


@router.get("/register", response_class=HTMLResponse)
async def get_register_page(request: Request):
    return templates.TemplateResponse(name='register.html', context={'request': request})


@router.get('/profile')
async def get_user_profile_page(request: Request):
    user = decode_access_token(request.cookies.get('users_access_token'))
    profile = get_user_by_nickname(user['name'])
    return templates.TemplateResponse(request=request, name='profile.html', context={
        'id': profile[0],
        'name': profile[1],
        'email': profile[2],
    })
