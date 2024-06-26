from fastapi import APIRouter,Depends,Path;
from category.schema.CategorySchema import CategoryRequest;
from category.service.CategoryService import CategoryService;
from fastapi.responses import JSONResponse;
from fastapi.encoders import jsonable_encoder;
from auth.jwt.JwtBearer import JwtBearer;

categoryController = APIRouter();

@categoryController.post('/category/',tags=['category'],response_model=dict,dependencies=[Depends(JwtBearer())])
def createCategory(request:CategoryRequest):
    response = CategoryService.createCategory(request);
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));

@categoryController.get('/category/{id}',tags=['category'],response_model=dict,dependencies=[Depends(JwtBearer())])
def getCategoryById(id:int = Path(ge=1)) -> dict:
    response = CategoryService.getCategoryById(id)
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));

@categoryController.put('/category/{id}',tags=['category'],response_model=dict,dependencies=[Depends(JwtBearer())])
def updateCategory(id:int, request:CategoryRequest)-> dict:
    response = CategoryService.updateCategory(id,request);
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));

@categoryController.delete('/category/{id}',tags=['category'],response_model=dict,dependencies=[Depends(JwtBearer())])
def deleteCategory(id: int = Path(ge=1)):
    response = CategoryService.deleteCategory(id);
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));
