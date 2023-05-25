from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuario, Post


# Destruir já existente e criar dnv
with app.app_context():
    database.drop_all()
    database.create_all()

# # Criar banco de dados
# with app.app_context():
#    database.create_all()
#
# with app.app_context():
#     usuario = Usuario(username='Henrique', email='henkle@gmail.com', senha='123456')
#     usuario2 = Usuario(username='João', email='joao@gmail.com', senha='123456')
#
#     # Adiciona a versão temporária
#     database.session.add(usuario)
#     database.session.add(usuario2)
#
#     # Salva
#     database.session.commit()
#
# with app.app_context():
#     meus_usuarios = Usuario.query.all() #.first() para pegar o primeiro
#     print(meus_usuarios)
#     usuario_teste = Usuario.query.filter_by(id=2).first()
#     print(usuario_teste)
#     print(usuario_teste.email)
#
# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo='Primeiro Post do Henrique.', corpo='Henrique voando')
#     database.session.add(meu_post)
#     database.session.commit()

# with app.app_context():
#     post = Post.query.first()
#     print(post.autor.username)
