from user.schema.UserSchema import UserRequest;
from passlib.context import CryptContext;
from user.models.User import User;
from auth.jwt.JwtManager import createToken;
from config.DataBase import SessionLocal;

bycrit = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    
    def login(request: UserRequest)-> dict:
        db = SessionLocal();
        existsUser = db.query(User).filter(User.name == request.name).first();
        
        if not existsUser:
            return {"message":"usuario no registrado"},{"status_code":401};
        
        if not bycrit.verify(request.password,existsUser.password):
            return {"message":"credenciales incorrectas"},{"status_code":401};
        
        return {"message":createToken({"user_name":existsUser.name})},{"status_code":200};