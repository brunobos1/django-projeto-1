from app.schemas import Alterar_BD, User_BD
from .model import Usuarios, Enderecos, session

class BD:

    def INSERT_BD(self, user: User_BD):

        usuario = Usuarios(nome=f'{user.nome}', email=f'{user.email}', cpf=f'{user.cpf}', pis=f'{user.pis}', 
        senha=f'{user.senha}', status=f'{user.status}')

        session.add(usuario)
        session.commit()

        id_user = self.SELECT_BD(user.email)

        endereco = Enderecos(id_usr=f'{id_user["id"]}', pais=f'{user.pais}', estado=f'{user.estado}', municipio=f'{user.municipio}',
        cep=f'{user.cep}', rua=f'{user.rua}', numero=f'{user.numero}', complemento=f'{user.complemento}',)

        session.add(endereco)
        session.commit()

    def SELECT_ALL_BD(self):

        result = []

        usuarios = (session.query(Usuarios).order_by(Usuarios.id).all())
        enderecos = (session.query(Enderecos).order_by(Enderecos.id).all())

        for u, e in zip(usuarios, enderecos):
            u = u.__dict__
            del u['_sa_instance_state']
            e = e.__dict__
            del e['_sa_instance_state']
            del e['id_usr']
            
            u.update(e)
            result.append(u)
        
        return result

    def SELECT_BD(self, login):

        usuarios = (session.query(Usuarios).order_by(Usuarios.id).all())

        for u in usuarios:

            if login == u.email or login == u.cpf or login == u.pis:
                usuario = u.__dict__
                del usuario['_sa_instance_state']

                endereco = session.query(Enderecos).filter_by(id_usr=usuario['id']).first()
                
                if endereco != None:
                    endereco = endereco.__dict__
                    del endereco['_sa_instance_state']
                    del endereco['id_usr']

                    usuario.update(endereco)
                
                return usuario
    
    def UPDATE_BD(self, user: Alterar_BD):

        usuario = session.query(Usuarios).filter_by(email=user['email']).first()
        endereco = session.query(Enderecos).filter_by(id_usr=usuario.id).first()

        usuario.nome = user['nome']
        usuario.email = user['email']
        usuario.cpf = user['cpf']
        usuario.pis = user['pis']
        usuario.senha = user['senha']
        endereco.pais = user['pais']
        endereco.estado = user['estado']
        endereco.municipio = user['municipio']
        endereco.cep = user['cep']
        endereco.rua = user['rua']
        endereco.numero = user['numero']
        endereco.complemento = user['complemento']

        session.commit()
                
    def DELETE_BD(self, login):

        usuarios = (session.query(Usuarios).order_by(Usuarios.id).all())

        for u in usuarios:

            if login == u.email or login == u.cpf or login == u.pis:
                usuario = session.query(Usuarios).filter_by(email=u.email).first()
                endereco = session.query(Enderecos).filter_by(id_usr=usuario.id).first()
                session.delete(endereco)
                session.delete(usuario)
                session.commit()
                break
                