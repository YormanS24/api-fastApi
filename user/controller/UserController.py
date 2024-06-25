from fastapi import APIRouter,Depends;
from fastapi.responses import JSONResponse;
from fastapi.encoders import jsonable_encoder;
from user.schema.UserSchema import UserRequest;
from config.DataBase import get_db;
from user.service.UserService import UserService;

userController = APIRouter();

@userController.post('/user/',tags=['user'],response_model=dict)
def createUser(request: UserRequest,session = Depends(get_db)):
    response = UserService.createUser(request,session);
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));