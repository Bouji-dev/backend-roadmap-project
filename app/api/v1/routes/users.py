from fastapi import APIRouter, status, HTTPException

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get('/', status_code=status.HTTP_200_OK)
def get_users():
    return {
        'data': [],
        'message': 'Users list'
    }

@router.get('/{user_id}', status_code=status.HTTP_200_OK)
def get_user(user_id: int):
    if user_id < 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='user_id must be greater than 0'
        )
    return {
        'id': user_id,
        'name': 'Test User'
    }
        
