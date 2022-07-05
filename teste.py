from backend.app.auth.auth_handler import signJWT

token = (signJWT('orlando75@gmail.com'))
print(token)