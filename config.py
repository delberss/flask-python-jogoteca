import os

## Variavel universal - CAPSLOCK ativado
SECRET_KEY = 'projeto_flask'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'admin',
        servidor = 'localhost',
        database = 'jogoteca'
    )


## devolve o caminho do diretorio - jogoteca
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'