from datetime import datetime, timedelta, timezone


def encode_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expire})
    # auth_data = get_auth_data()
    # encode_jwt = jwt.encode(to_encode, auth_data['secret_key'], algorithm=auth_data['algorithm'])
    return to_encode


def decode_access_token(token: str) -> dict:
    pass
