from flask import Flask
from init import db, ma, bcrypt, jwt
import os

def create_app():
    app = Flask(__name__)

    app.json.sort_keys = False #Returns fields in specified order

    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URI")

    app.config["JWT_SECRET_KEY"]=os.environ.get("JWT_SECRET_KEY")



    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from controllers.cli_controller import db_commands
    app.register_blueprint(db_commands)

    from controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    from controllers.order_controller import orders_bp
    app.register_blueprint(orders_bp)

    return app