from app import create_app
from flask_principal import Principal


app = create_app()
principals = Principal(app)

if __name__ == '__main__':
    app.run(debug=True)