from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from config import web_api_config
import sys
import model
import uvicorn
from router.signin import router as signinRouter
from router.groups import router as groupsRouter
sys.dont_write_bytecode = True


app = FastAPI()

# FIXME: テスト環境用
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def request_validation_handler(req, exc):
    return JSONResponse(status_code=400, content={"code": "InvalidParameter"})

app.include_router(signinRouter)
app.include_router(groupsRouter)


def main():
    uvicorn.run('main:app',
                port=int(web_api_config.get("PORT")),
                host=web_api_config.get("HOST"),
                reload=True,
                ssl_keyfile=web_api_config.get("SSL_KEY"),
                ssl_certfile=web_api_config.get("SSL_CRT"))


if __name__ == '__main__':
    main()
