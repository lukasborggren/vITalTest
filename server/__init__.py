from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from server.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from server import routes
