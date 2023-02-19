from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password):
    return pwd_context.hash(password)

def verify(c_password,h_password):
    return pwd_context.verify(hash(c_password),h_password)