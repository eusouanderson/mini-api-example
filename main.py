from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Estrutura para simular banco de dados em memória
users_db: Dict[str, str] = {}


class User(BaseModel):
    username: str
    password: str

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/signup")
def signup(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Usuário já existe")
    users_db[user.username] = user.password
    print(users_db)
    return {"message": "Usuário cadastrado com sucesso!"}

@app.post("/login")
def login(user: User):
    if user.username not in users_db or users_db[user.username] != user.password:
        raise HTTPException(status_code=400, detail="Credenciais incorretas")
    return {"message": "Login bem-sucedido!"}
