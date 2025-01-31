from src.models import User
from src.repositories.user_repository import UserRepository
from src.unit_of_work import UnitOfWork
import pytest

@pytest.fixture
def user_repository():
    uow = UnitOfWork()
    return UserRepository(uow)

@pytest.fixture
def sample_user():
    return User(name="Test User", email="test@example.com", hashed_password="hashed_password")

def test_create_user(user_repository, sample_user):
    user_repository.add(sample_user)
    user_repository.uow.commit()
    assert sample_user.id is not None

def test_get_user(user_repository, sample_user):
    user_repository.add(sample_user)
    user_repository.uow.commit()
    retrieved_user = user_repository.get(sample_user.id)
    assert retrieved_user.email == sample_user.email

def test_update_user(user_repository, sample_user):
    user_repository.add(sample_user)
    user_repository.uow.commit()
    sample_user.name = "Updated User"
    user_repository.update(sample_user)
    user_repository.uow.commit()
    updated_user = user_repository.get(sample_user.id)
    assert updated_user.name == "Updated User"

def test_delete_user(user_repository, sample_user):
    user_repository.add(sample_user)
    user_repository.uow.commit()
    user_repository.delete(sample_user.id)
    user_repository.uow.commit()
    deleted_user = user_repository.get(sample_user.id)
    assert deleted_user is None

def test_user_leaderboard(user_repository):
    user1 = User(name="User One", email="user1@example.com", hashed_password="hashed_password")
    user2 = User(name="User Two", email="user2@example.com", hashed_password="hashed_password")
    user_repository.add(user1)
    user_repository.add(user2)
    user_repository.uow.commit()
    leaderboard = user_repository.get_leaderboard()
    assert len(leaderboard) >= 2  # Assuming the leaderboard returns at least two users