from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from jose import JWTError, jwt
from config.settings import app_config
 
class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
 
    async def __call__(self, request: Request):
        credentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")
 
    def verify_jwt(self, token: str) -> bool:
        try:
            payload = jwt.decode(token, app_config["SECRET_KEY"], algorithms=app_config["ALGORITHM"])
            print("Decoded Payload:", payload)  
            return True
        except JWTError:
            return False