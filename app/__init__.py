from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
config = "config.DevelopmentConfig"
    
def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    
    from .views import views
    app.register_blueprint(views, url_prefix = '/')

    from .auth import auth
    app.register_blueprint(auth, url_prefix = '/')

    from .models import User, Course
    with app.app_context():
        db.create_all()
    
    loginManager = LoginManager(app)
    loginManager.login_view = "auth.login"
    loginManager.init_app(app)
    
    @loginManager.user_loader
    def load_user(id):
        return User.query.get(int(id))  

    return app
