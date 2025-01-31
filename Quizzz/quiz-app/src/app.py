from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.config import Config
from src.views.auth_views import auth_bp
from src.views.quiz_views import quiz_bp
from src.views.user_views import user_bp

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(auth_bp)
app.register_blueprint(quiz_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)