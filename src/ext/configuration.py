import os
from dotenv import load_dotenv

load_dotenv()
def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE")
    app.secret_key = os.getenv('SECRET_KEY')
