from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DEBUG: bool
    ALLOWED_HOSTS: str
    MCQ_PER_PAGE: int
    LIFELINE_50_50: bool
    LIFELINE_SKIP: bool
    HINTS_ENABLED: bool
    IMAGE_BASE_QUESTIONS: bool
    AUDIO_BASE_QUESTIONS: bool

    class Config:
        env_file = ".env"

settings = Settings()