from fastapi import FastAPI
from routes.produto_route import router as produto_router

app = FastAPI()

app.include_router(produto_router)