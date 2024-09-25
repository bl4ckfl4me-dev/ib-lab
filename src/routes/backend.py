from fastapi import APIRouter, Request, Response, HTTPException
from cript import encode_access_token, decode_access_token
from db.crud import get_user_with_auth, add_new_user
from db.exceptions import UserWithThisEmailAlreadyPresented
from models import UserAuth

router = APIRouter()


@router.post('/add_new_user')
async def add_user_endpoint(request: Request):
    user_data = await request.json()

    if user_data['password'] != user_data['confirm_password']:
        return {'ok': False, 'message': 'Пароли не совпадают'}
    
    try:
        add_new_user(user_data['email'], user_data['username'], user_data['password'])
    except UserWithThisEmailAlreadyPresented:
        return {'ok': False, 'message': 'Пользователь с такой почтой уже существует'}

    return {'ok': True, 'message': 'Successfully added new user'}


@router.post("/authenticate_user")
async def authenticate_user(response: Response, user_data: UserAuth):
    user = get_user_with_auth(email=user_data.email, password=user_data.password)
    if user is None:
        raise HTTPException(status_code=400, detail='Incorrect email or password')
    access_token = encode_access_token(user)
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'ok': True, 'access_token': access_token, 'message': 'Auth succeed!'}
