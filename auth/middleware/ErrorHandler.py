from starlette.middleware.base import BaseHTTPMiddleware;
from fastapi import FastAPI, Request;
from starlette.responses import Response;
from fastapi.responses import JSONResponse;

class ErrorHandler(BaseHTTPMiddleware):
    
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app);
        
    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request);
        except Exception as ex:
            return  JSONResponse(status_code=403,content={"message":"no tienes permisos para acceder a este recurso"});