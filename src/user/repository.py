from src.base_repository import BaseRepository
from src.user.models import User


class UserRepository(BaseRepository[User]):
    model = User
