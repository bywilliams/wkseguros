import os

from dotenv import load_dotenv
from flask import Flask
from flask_wtf import CSRFProtect

from .routes import register_routes

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
csrf = CSRFProtect(app)

register_routes(app)
