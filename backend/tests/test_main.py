from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.model import Base, session
from main import app, verify_password
from app.auth.auth_handler import signJWT

DATABASE_URL = 'sqlite:///./test.db'

engine = create_engine(DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[session] = override_get_db

client = TestClient(app)

def test_get_root():
    response = client.get("/")
    body = response.json()
    assert response.status_code == 200
    assert "Olá, para usar a API no navegador adicione /docs na url." in body["Boas-vindas"] 

def test_cadastro_usuario():

    response = client.post(
        '/cadastrar',
        json={'nome': 'Orlando de Machado', 'email': 'orlando75@gmail.com', 'cpf': '065.776.060-99', 'pis': '637.98692.53-5',
        'senha': '741123', 'pais':'Brasil', 'estado': 'Bahia', 'municipio': 'Salvador', 'cep': '41635153', 'rua': 'Rua Nossa Senhora da Esperança',
        'numero': '215', 'complemento': 'Apartamento 114'},
    )

    assert response.status_code == 200
    data = response.json()
    data = data['data']
    assert data['email'] == 'orlando75@gmail.com'
    assert verify_password('741123', data['senha'])

def teste_post_login():
    response = client.post(
        '/token',
        headers={'Content-Type': 'application/json'},
        json={'login': 'orlando75@gmail.com', 'senha': '741123'},
        )

    assert response.status_code == 200

def test_alterar_usuario():

    token = (signJWT('orlando75@gmail.com'))

    response = client.put(
        '/alterar', headers={'accept': 'application/json', 'Authorization': f'Bearer {token}'},
        json={'nome': 'Orlando de Machado Assis', 'senha': '741123', 'pais':'Brasil', 'estado': 'Bahia', 
        'municipio': 'Salvador', 'cep': '41635153', 'rua': 'Rua Nossa Senhora da Esperança',
        'numero': '215', 'complemento': 'Apartamento 114'},
    )
    assert response.status_code == 200
    data = response.json()
    data = data['data']
    assert data['nome'] == 'Orlando de Machado Assis'
    assert verify_password('741123', data['senha'])

def test_deletar_usuario():

    token = (signJWT('orlando75@gmail.com'))

    response = client.delete('/deletar', headers={'accept': 'application/json', 'Authorization': f'Bearer {token}'})
    assert response.status_code == 200