from pydantic import BaseModel, Field

class UserLoginSchema(BaseModel):
    login: str = Field(...)
    senha: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "login": "jose@x.com",
                "senha": "weakpassword"
            },
        }
    

class User(BaseModel):
    
    nome: str = Field(...)
    email: str = Field(...)
    cpf: str = Field(...)
    pis: str = Field(...)
    senha: str = Field(...)
    pais: str = Field(...)
    estado: str = Field(...)
    municipio: str = Field(...)
    cep: str = Field(...)
    rua: str = Field(...)
    numero: str = Field(...)
    complemento = ''
    status = 'Ativo'

    class Config:
        schema_extra = {
            "example": {
                "nome": "José Silva Cardoso",
                "email": "jose@x.com",
                "cpf": "70883148005",
                "pis": "03669683820",
                "senha": "weakpassword",
                "pais": "Brasil",
                "estado": "Bahia",
                "municipio": "Salvador",
                "cep": "41635153",
                "rua": "Rua Nossa Senhora da Esperança",
                "numero": "215",
                "complemento": "Apartamento 114"
            }
        }

class User_BD(BaseModel):
    
    nome= ''
    email= ''
    cpf= ''
    pis= ''
    senha= ''
    pais= ''
    estado= ''
    municipio= ''
    cep= ''
    rua= ''
    numero= ''
    complemento = ''
    status = 'Ativo'

class AlterarUser(BaseModel):
    
    nome: str = Field(...)
    email = ''
    cpf = ''
    pis = ''
    senha: str = Field(...)
    pais: str = Field(...)
    estado: str = Field(...)
    municipio: str = Field(...)
    cep: str = Field(...)
    rua: str = Field(...)
    numero: str = Field(...)
    complemento = ''
    status = 'Ativo'

    class Config:
        schema_extra = {
            "example": {
                "nome": "",
                "senha": "",
                "pais": "",
                "estado": "",
                "municipio": "",
                "cep": "",
                "rua": "",
                "numero": "",
                "complemento": "",
            }
        }

class Alterar_BD(BaseModel):
    
    nome= ''
    email= ''
    cpf= ''
    pis= ''
    senha= ''
    pais= ''
    estado= ''
    municipio= ''
    cep= ''
    rua= ''
    numero= ''
    complemento = ''
    status = 'Ativo'