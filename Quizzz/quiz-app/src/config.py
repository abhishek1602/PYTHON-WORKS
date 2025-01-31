from os import environ

class Config:
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or 'postgresql://user:password@localhost/quiz_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = environ.get('SECRET_KEY') or 'your_secret_key'
    DEBUG = environ.get('DEBUG', 'False') == 'True'
    SESSION_PERMANENT = False
    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = 3600  # 1 hour
    HINTS_ENABLED = True
    LIFELINES_ENABLED = True
    TIMER_DURATION = 60  # seconds per question
    MAX_QUESTIONS = 10  # maximum number of questions per quiz
    LEADERBOARD_LIMIT = 10  # number of top users to display on leaderboard