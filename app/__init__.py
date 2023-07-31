from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
config = "config.DevelopmentConfig"
    
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "wqeqweewefddvcxaxsdf3456"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://align_db_user:YgKqcbRp1KD0zGrRMS0X7lwSj8LCv9Wj@dpg-cj3piv98g3n1jkjaca0g-a/align_db_3gvy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
