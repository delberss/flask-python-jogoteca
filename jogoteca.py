from flask import Flask

##O SQLAlchemy é uma biblioteca de mapeamento objeto-relacional (ORM) para Python.
# Ele fornece uma maneira de interagir com bancos de dados relacionais usando uma abordagem
# orientada a objetos, em vez de escrever consultas SQL diretamente.
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

## __name__ é para fazer referencia ao arquivo em questão
app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

from views_game import *
from views_user import *

if __name__ == '__main__':
    app.run(debug=True)
