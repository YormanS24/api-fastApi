from fastapi import APIRouter,Depends,Path;
from fastapi.encoders import jsonable_encoder;
from fastapi.responses import JSONResponse;
from movie.schema.MovieSchema import MovieRequest,MovieUpdateRequest;
from movie.service.MovieService import MovieService;
from auth.jwt.JwtBearer import JwtBearer;

movieController = APIRouter();

@movieController.post('/movie/',tags=['movie'],response_model=dict,dependencies=[Depends(JwtBearer())])
def createMovie(request:MovieRequest) -> dict:
    response = MovieService.createMovie(request);
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));

@movieController.get('/movie/{id}',tags=['movie'],response_model=dict,dependencies=[Depends(JwtBearer())])
def getMovie(id:int = Path(ge=1))-> dict:
    response = MovieService.getMovie(id);
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));

@movieController.put('/movie/{id}',tags=['movie'],response_model=dict,dependencies=[Depends(JwtBearer())])
def updateMovie(request: MovieUpdateRequest,id: int = Path(ge=1)):
    response = MovieService.updateMovie(request,id);
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));

@movieController.delete('/movie/{id}',tags=['movie'],response_model=dict,dependencies=[Depends(JwtBearer())])
def deleteMovie(id: int = Path(ge=1))-> dict:
    response = MovieService.deleteMovie(id);
    return JSONResponse(status_code=response[1]['status_code'],content=jsonable_encoder(response[0]));
