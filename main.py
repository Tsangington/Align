from app import create_app

config = "config.DevelopmentConfig"
app = create_app(config)

if __name__ == '__main__':
    app.run(debug=True)