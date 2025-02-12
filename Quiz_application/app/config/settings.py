from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:admin1234@localhost/quiz_database" 
    SECRET_KEY: str = "quiz_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30 

    class Config: 
        env_file = ".env"

settings = Settings()
   