from fastapi import FastAPI;
from category.controller.CategoryController import categoryController;
from movie.controller.MovieController import movieController;
from user.controller.UserController import userController;
from config.DataBase import Base,engine;
from auth.controller.AuthController import authController;
from auth.middleware.ErrorHandler import ErrorHandler;

app = FastAPI();
app.include_router(categoryController);
app.include_router(movieController);
app.include_router(userController);
app.include_router(authController);
app.add_middleware(ErrorHandler);

Base.metadata.create_all(bind=engine);

app.title = "Api Basico FastApi";
app.description = "primera implementacion de fast-api";
app.version = "0.0.1";