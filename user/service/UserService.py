from user.schema.UserSchema import UserRequest;
from sqlalchemy.orm import Session;
from user.models.User import User;
from passlib.context import CryptContext;

bycrit = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    
    def createUser(request:UserRequest,db: Session)-> dict:
        existsUser = db.query(User).filter(User.name == request.name).first();
        
        if existsUser: 
            return {"message":"ya se encuentra un usuario resgistrado con el mismo nombre"},{"status_code":409};
              
        request.password = bycrit.hash(request.password);
        db.add(User(**request.model_dump()));
        db.commit();
        
        return {"message":"usuario registrado con exito"},{"status_code":201};