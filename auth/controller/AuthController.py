from fastapi import APIRouter;
from fastapi.responses import JSONResponse;
from user.schema.UserSchema import UserRequest;
from auth.service.AuthService import AuthService;
from fastapi.encoders import jsonable_encoder;

authController = APIRouter();

@authController.post('/auth/login',tags=['authentication'],response_model=dict)
def login(request: UserRequest)-> dict:
    response = AuthService.login(request);
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));