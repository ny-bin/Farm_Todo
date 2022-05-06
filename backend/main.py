from typing import List
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from routers import route_todo, route_auth
from schemas import CsrfSettings, SuccessMsg
from fastapi_csrf_protect import CsrfProtect
from fastapi_csrf_protect.exceptions import CsrfProtectError
from fastapi.openapi.utils import get_openapi

swagger_ui_default_parameters = {
    "dom_id": "#swagger-ui",
    "layout": "BaseLayout",
    "deepLinking": True,
    "showExtensions": True,
    "showCommonExtensions": True,
}
app = FastAPI(swagger_ui_parameters=swagger_ui_default_parameters)
app.include_router(route_todo.router)
app.include_router(route_auth.router)

origins = [
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@CsrfProtect.load_config
def get_csrf_config():
    return CsrfSettings()


@app.get("/", response_model=SuccessMsg)
def root():
    return {"message": "welcome to fast api"}


@app.exception_handler(CsrfProtectError)
def csrf_protect_exception_handler(request: Request, exc: CsrfProtectError):
    return JSONResponse(
        status_code=exc.status_code,
        content={'detail': exc.message
                 }
    )
