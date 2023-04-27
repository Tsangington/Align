from app import create_app
from flask_principal import Principal

config = "config.DevelopmentConfig"
app = create_app(config)
principals = Principal(app)

if __name__ == '__main__':
    app.run(debug=True)