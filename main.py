from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.produto_route import router as produto_router

app = FastAPI()

# LIBERAR CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(produto_router)
