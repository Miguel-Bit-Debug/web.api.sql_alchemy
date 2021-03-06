from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def config_db(app):
    db.init_app(app)
    app.db = db

    return db