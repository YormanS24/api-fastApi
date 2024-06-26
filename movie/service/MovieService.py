from movie.schema.MovieSchema import MovieRequest,MovieUpdateRequest;
from movie.models.Movie import Movie;
from category.models.Category import Category;
from config.DataBase import SessionLocal;

class MovieService:
    
    def createMovie(request: MovieRequest)-> dict:
        db = SessionLocal();
        
        if not db.query(Category).filter(Category.categoryId == request.categoryId).first():
            return {"message":"la categoria no se encuentra resgitrada"},{"status_code":404};

        
        existMovie = db.query(Movie).filter(Movie.name == request.name).first();
        if existMovie:
            return {"message":"ya se encuentra registrada la pelicula"},{"status_code":409};
        
        db.add(Movie(**request.model_dump()));
        db.commit();
        
        return {"message":"pelicula fue registrada con exito"},{"status_code":201};
    
    def getMovie(id:int)-> dict:
        db = SessionLocal();
        
        existMovie = db.query(Movie).filter(Movie.movieId == id).first();
        
        if not existMovie:
            return {"message":"la pelicula no se encuentra"},{"status_code":404};
        
        return {"message":existMovie},{"status_code":200};
    
    def updateMovie(request: MovieUpdateRequest,id: int)->dict:
        db = SessionLocal();
        
        existMovie = db.query(Movie).filter(Movie.movieId == id).first();
        
        if not existMovie: 
            return {"message":"la pelicula no se encuentra"},{"status_code":404};
        
        existMovie.name = request.name;
        existMovie.description = request.description;
        db.commit();
        
        return {"message":"pelicula actualizada con exito"},{"status_code":200};
    
    def deleteMovie(id: int) -> dict:
        db = SessionLocal();
        
        existMovie = db.query(Movie).filter(Movie.movieId == id).first();
        
        if not existMovie:
            return {"message":"ya se encuentra registrada la pelicula"},{"status_code":404};
        
        db.delete(existMovie);
        db.commit();
        
        return {"message":"pelicula eliminada con exito"},{"status_code":200};

        
        
