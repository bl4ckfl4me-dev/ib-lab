from fastapi import APIRouter, Request, Response, HTTPException
from cript import encode_access_token, decode_access_token
from db.crud import get_user_with_auth, add_new_user
from db.exceptions import UserWithThisEmailAlreadyPresented
from fastapi.responses import JSONResponse
from db.exceptions import UserNotPresented, PasswordNotMatched
from models import UserAuth

router = APIRouter()


@router.post('/add_new_user')
async def add_user_endpoint(request: Request):
    user_data = await request.json()

    if user_data['password'] != user_data['confirm-password']:
        return {'ok': False, 'message': 'Пароли не совпадают'}
    
    try:
        add_new_user(user_data['email'], user_data['username'], user_data['password'])
    except UserWithThisEmailAlreadyPresented:
        return {'ok': False, 'message': 'Пользователь с такой почтой уже существует'}

    return {'ok': True, 'message': 'Successfully added new user'}


@router.post("/authenticate_user")
async def authenticate_user(request: Request):
    user_data = await request.json()
    try:
        user = get_user_with_auth(user_data['username'], user_data['password'])
    except UserNotPresented:
        raise HTTPException(status_code=400, detail='User not presented')
    except PasswordNotMatched:
        raise HTTPException(status_code=400, detail='Invalid password')

    access_token = encode_access_token(user)
    response = JSONResponse({
        'ok': True, 'access_token': access_token, 'message': 'Auth succeed!'
    })
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return response
