from fastapi import FastAPI, Body, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import AlterarUser, User, UserLoginSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT
from passlib.context import CryptContext
from app.valida_cpf import valida_cpf
from app.database import crud

##################### Variaveis Globais #####################

app = FastAPI(title='Sistema de cadastro/login')

origins = {
    "http://localhost",
    "http://localhost:3000",
    "https://aplicacao-1-login.web.app"
}

app.add_middleware(
   CORSMiddleware,
    allow_origins = origins,
    allow_credentials =True,
    allow_methods = ["*"],
    allow_headers= ["*"],
)

db = crud.BD()

usuario_atual = ''

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

##################### Funções de verificação de usuário #####################

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def check_user(user: UserLoginSchema):
    u = db.SELECT_BD(user.login)

    if u != None:
        if verify_password(user.senha, u['senha']) and u['status'] == 'Ativo':
            return True

    return False

##################### Modulos da API #####################

@app.get("/", tags=["Inicio"])
def comecar():

    return {"Boas-vindas": "Olá, para usar a API no navegador adicione /docs na url. A API é livre para qualquer um se cadastrar, mas atenção " 
        "pois você só poderá usar seu CPF, email e PIS uma vez, caso você cadastre o email incorreto, com o PIS e CPF corretos, por exemplo, "
        "você precisará deleter o seu usuário e cria-lo novamente, pois a opção de alterar usuário não permite a alteração do PIS, CPF ou E-mail, "
        "pois são dados vitais para validarmos a conta de cada um."}

@app.post("/token", tags=["Login"])
def login(user: UserLoginSchema = Body(...)):
    if check_user(user):

        global usuario_atual
        usuario_atual = user.login

        nome_atual = db.SELECT_BD(usuario_atual)['nome']

        return {'token': signJWT(user.login), 'nome_usuario': nome_atual}

    return JSONResponse(status_code=401, content={'mensagem': 'Usuário ou senha incorretos.'})

@app.post("/cadastrar", tags=["Cadastro"])
def criar_usuario(user: User = Body(...)):
            
    users = db.SELECT_ALL_BD()

    user.senha = get_password_hash(user.senha)
    user.cpf = (user.cpf.replace('.','')).replace('-','')
    user.pis = (user.pis.replace('.','')).replace('-','')

    for u in users:
        if user.cpf == u['cpf'] or user.email == u['email'] or user.pis == u['pis']:
            return JSONResponse(status_code=400, content={'mensagem': 'Já existe um cadastro com essas informações'})

    if not len(user.cpf) == 11 or not valida_cpf(user.cpf):
        return JSONResponse(status_code=400, content={'mensagem': 'CPF inválido'})
    
    if len(user.pis) > 11 or len(user.pis) < 10:
        return JSONResponse(status_code=400, content={'mensagem': 'PIS inválido'})

    db.INSERT_BD(user)

    usuario_consulta = db.SELECT_BD(user.email)

    return JSONResponse(status_code=200, content={'mensagem': 'Usuário criado com sucesso', 'data': usuario_consulta})

@app.put("/alterar", dependencies=[Depends(JWTBearer())], tags=["Cadastro"])
def alterar_usuario(user: AlterarUser = Body(...)):
    
    global usuario_atual
    usuario = db.SELECT_BD(usuario_atual)
    user = dict(user)

    user['email'] = usuario['email']
    user['cpf'] = usuario['cpf']
    user['pis'] = usuario['pis']

    keys = user.keys()
    for key in keys:
        if user[key] == '':
            user[key] = usuario[key]

    try:
        if user['senha'] != '':
            user['senha'] = get_password_hash(user['senha'])

        db.UPDATE_BD(user)

        user_alterado = db.SELECT_BD(user['email'])

        return JSONResponse(status_code=200, content={'mensagem': 'Usuário alterado com sucesso', 'data': user_alterado})

    except Exception as e:

        return JSONResponse(status_code=500, content={'mensagem': 'Ocorreu um erro ao alterar o cadastro.', 'data': e})

@app.delete("/deletar", dependencies=[Depends(JWTBearer())], tags=["Cadastro"])
def deletar_usuario():

    db.DELETE_BD(usuario_atual)

    teste_del = db.SELECT_BD(usuario_atual)

    if teste_del != None:
        return JSONResponse(status_code=500, content={'mensagem': 'Ocorreu um erro ao deletar o usuário.'})
    
    return JSONResponse(status_code=200, content={'mensagem': 'Usuário deletado com sucesso'})

