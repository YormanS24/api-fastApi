from fastapi import APIRouter,Depends,Path;
from fastapi.encoders import jsonable_encoder;
from fastapi.responses import JSONResponse;
from movie.schema.MovieSchema import MovieRequest,MovieUpdateRequest;
from config.DataBase import get_db;
from movie.service.MovieService import MovieService;
from auth.jwt.JwtBearer import JwtBearer;

movieController = APIRouter();

@movieController.post('/movie/',tags=['movie'],response_model=dict,dependencies=[Depends(JwtBearer())])
def createMovie(request:MovieRequest,session = Depends(get_db)) -> dict:
    response = MovieService.createMovie(request,session);
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));

@movieController.get('/movie/{id}',tags=['movie'],response_model=dict,dependencies=[Depends(JwtBearer())])
def getMovie(id:int = Path(ge=1),session = Depends(get_db))-> dict:
    response = MovieService.getMovie(id,session);
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));

@movieController.put('/movie/{id}',tags=['movie'],response_model=dict,dependencies=[Depends(JwtBearer())])
def updateMovie(request: MovieUpdateRequest,id: int = Path(ge=1),session = Depends(get_db)):
    response = MovieService.updateMovie(request,id,session);
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));

@movieController.delete('/movie/{id}',tags=['movie'],response_model=dict,dependencies=[Depends(JwtBearer())])
def deleteMovie(id: int = Path(ge=1),session = Depends(get_db))-> dict:
    response = MovieService.deleteMovie(session,id);
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));
