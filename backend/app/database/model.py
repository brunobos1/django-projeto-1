from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import os
from dotenv import find_dotenv, load_dotenv 

load_dotenv(find_dotenv())

engine = create_engine(os.getenv("DATABASE_URL"))

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    email = Column(String(100))
    cpf = Column(String(100))
    pis = Column(String(100))
    senha = Column(String(100))
    status = Column(String(100), default='Ativo')

    enderecos = relationship('Enderecos')

    def __repr__(self):
        retorno = f'id: {self.id}, nome: {self.nome}, email: {self.email}, cpf: {self.cpf}, pis: {self.pis}, senha: {self.senha}, status: {self.status}'
        return '{' + retorno + '}'

class Enderecos(Base):
    __tablename__ = 'enderecos'
    id = Column(Integer, primary_key=True)
    pais = Column(String(50))
    estado = Column(String(100))
    municipio = Column(String(100))
    cep = Column(String(10))
    rua = Column(String(100))
    numero = Column(Integer)
    complemento = Column(String(100))

    id_usr = Column(Integer, ForeignKey("usuarios.id"))

    def __repr__(self):
        retorno = f'id_usuario:{self.id_usr}, pais: {self.pais}, estado: {self.estado}, municipio: {self.municipio}, \
        cep: {self.cep}, rua: {self.rua}, numero: {self.numero}, complemento: {self.complemento}'
        return '{' + retorno + '}'

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()