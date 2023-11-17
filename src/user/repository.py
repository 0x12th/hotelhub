from base_repository import BaseRepository
from user.models import User


class UserRepository(BaseRepository[User]):
    model = User
