from fastapi import APIRouter;
from fastapi.responses import JSONResponse;
from fastapi.encoders import jsonable_encoder;
from user.schema.UserSchema import UserRequest;
from user.service.UserService import UserService;

userController = APIRouter();

@userController.post('/user/',tags=['user'],response_model=dict)
def createUser(request: UserRequest):
    response = UserService.createUser(request);
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));