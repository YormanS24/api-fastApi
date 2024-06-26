from fastapi import HTTPException,Request;
from fastapi.security import HTTPBearer;
from auth.jwt.JwtManager import validateToken;
from config.DataBase import SessionLocal;
from user.models.User import User;

class JwtBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request);
        data = validateToken(auth.credentials);
        db = SessionLocal();
        
        if not db.query(User).filter(User.name == data['user_name']).first():
            raise HTTPException(status_code=403,detail={"message":"actualmente no te encuentras registrado"});