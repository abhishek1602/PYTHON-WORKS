from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum

class Difficulty(enum.Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"

class MCQ(Base):
    __tablename__ = "mcqs"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text, nullable=False)
    option_a = Column(String, nullable=False)
    option_b = Column(String, nullable=False)
    option_c = Column(String, nullable=False)
    option_d = Column(String, nullable=False)
    correct_answer = Column(String, nullable=False)
    category = Column(String, nullable=False)
    difficulty = Column(Enum(Difficulty), nullable=False)
    explanation = Column(Text, nullable=True)
    tags = Column(String, nullable=True)  # Comma-separated tags for bookmarking

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="mcqs")  # Assuming a User model exists with a relationship

    def __repr__(self):
        return f"<MCQ(id={self.id}, question={self.question}, correct_answer={self.correct_answer})>"