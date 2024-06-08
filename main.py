from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import ITopNResponse

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://127.0.0.1",
    "http://127.0.0.1:5173",
    "https://wonderful-bay-0ec57fa0f.5.azurestaticapps.net"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/top-n/{n}", response_model=ITopNResponse)
async def top_n(n: int):
    """
    Get top n

    - **n**: n

    Returns n
    """
    return { "data": n }

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


