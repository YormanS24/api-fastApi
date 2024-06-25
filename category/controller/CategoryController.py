from fastapi import APIRouter,Depends,Path;
from category.schema.CategorySchema import CategoryRequest;
from category.service.CategoryService import CategoryService;
from fastapi.responses import JSONResponse;
from fastapi.encoders import jsonable_encoder;
from config.DataBase import get_db;
from auth.jwt.JwtBearer import JwtBearer;

categoryController = APIRouter();

@categoryController.post('/category/',tags=['category'],response_model=dict,dependencies=[Depends(JwtBearer())])
def createCategory(request:CategoryRequest,Session = Depends(get_db)):
    response = CategoryService.createCategory(request,Session);
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));

@categoryController.get('/category/{id}',tags=['category'],response_model=dict,dependencies=[Depends(JwtBearer())])
def getCategoryById(id:int = Path(ge=1),Session = Depends(get_db)) -> dict:
    response = CategoryService.getCategoryById(id,Session)
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));

@categoryController.put('/category/{id}',tags=['category'],response_model=dict,dependencies=[Depends(JwtBearer())])
def updateCategory(id:int, request:CategoryRequest,Session = Depends(get_db))-> dict:
    response = CategoryService.updateCategory(id,Session,request);
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));

@categoryController.delete('/category/{id}',tags=['category'],response_model=dict,dependencies=[Depends(JwtBearer())])
def deleteCategory(id: int = Path(ge=1),Session = Depends(get_db)):
    response = CategoryService.deleteCategory(id,Session);
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));
