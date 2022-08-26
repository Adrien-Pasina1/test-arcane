from flask import Flask
from src.schemas import ma
from src.models import db

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///./database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)

    from src.views.property_view import property_bp
    app.register_blueprint(property_bp)
    from src.views import users_bp
    app.register_blueprint(users_bp)

    @app.before_first_request
    def create_table():
        db.create_all()

    return app
