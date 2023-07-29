from app import app

if __name__ == "__main__":
    app.run()

# gunicorn wsgi_server:app -b 0.0.0.0:8000