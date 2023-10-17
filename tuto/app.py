from flask import Flask
from flask_bootstrap import Bootstrap5
app = Flask(__name__)
app.config['BOOTSRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap5(app)

import os.path
def mkpath(p):
    return os.path.normpath(
        os.path.join(
            os.path.dirname(__file__),
        p))

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('../myapp.db'))
db = SQLAlchemy(app)
app.config['SECRET_KEY']='F8979C05-576E-4042-BEE0-7AC89369C641'