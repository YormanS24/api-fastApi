from user.schema.UserSchema import UserRequest;
from sqlalchemy.orm import Session;
from passlib.context import CryptContext;
from user.models.User import User;
from auth.jwt.JwtManager import createToken;

bycrit = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    
    def login(request: UserRequest,db: Session)-> dict:
        existsUser = db.query(User).filter(User.name == request.name).first();
        
        if not existsUser:
            return {"message":"usuario no registrado"},{"status_code":401};
        
        if not bycrit.verify(request.password,existsUser.password):
            return {"message":"credenciales incorrectas"},{"status_code":401};
        
        return {"message":createToken({"user_name":existsUser.name})},{"status_code":200};