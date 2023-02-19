from jose import JWTError,jwt
from datetime import datetime,timedelta 

SECRET_KEY = "idris@abkar@2014"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_jwt(data : dict):
    data_to_encode = data.copy()

    expire_time = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data_to_encode.update({"exp" : expire_time})
    jw_token = jwt.encode(data_to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return jw_token