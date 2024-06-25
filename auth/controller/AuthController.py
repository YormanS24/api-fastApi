from fastapi import APIRouter,Depends;
from fastapi.responses import JSONResponse;
from user.schema.UserSchema import UserRequest;
from config.DataBase import get_db;
from auth.service.AuthService import AuthService;
from fastapi.encoders import jsonable_encoder;

authController = APIRouter();

@authController.post('/auth/login',tags=['authentication'],response_model=dict)
def login(request: UserRequest,session = Depends(get_db))-> dict:
    response = AuthService.login(request,session);
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));