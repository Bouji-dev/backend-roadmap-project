from app.core.exceptions import NotFoundException


class UserService:
    def get_user(self, user_id: int) -> dict:
        if user_id != 1:
            raise NotFoundException('User not found')
        
        return {
            'id': 1,
            'name': 'Ehsan'
        }