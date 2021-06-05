from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated = "auto")

class Hash():
    def bcrypt(password):
        return pwd_cxt.hash(password)

    def verify(plain_pwd,hashed_pwd):
        return pwd_cxt.verify(plain_pwd, hashed_pwd)