from fastapi import Depends,HTTPException,status
from fastapi.security.oauth2 import OAuth2PasswordBearer
from jose import JWTError,jwt
from datetime import datetime,timedelta 
from app import schemas
from app.settings import settings



oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MUNITES

def create_jwt(data : dict):
    data_to_encode = data.copy()

    expire_time = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data_to_encode.update({"exp" : expire_time})
    jw_token = jwt.encode(data_to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return jw_token

def verify_token(token : str,credentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id : str = payload.get("user_id") 
        if id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    token_data = schemas.TokenData(user_id=id,user_name=payload.get("user_name"))
    return token_data


def get_current_user(token : str = Depends(oauth_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credentials",headers={"WWW-Authenticate" : "Bearer"})
    user_id = verify_token(token=token,credentials_exception=credentials_exception).user_id
    return user_id