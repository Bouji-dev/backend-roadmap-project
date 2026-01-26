from fastapi import APIRouter, status, HTTPException, Query
from app.schemas.user import UserCreate, UserResponse
from typing import Optional


router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.get('/')
def get_users(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    min_age: Optional[int] = Query(None, ge=0),
    sort: Optional[str] = Query('asc')
):
    offset = (page - 1) * page_size

    if sort not in ('asc','desc'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="sort must be 'asc' or 'desc'"
        )
    if page_size > 50:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='page size must be less than 50'
        )
    
    return {
        'page': page,
        'page_size': page_size,
        'total': 0,
        'items': []
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
        
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: UserCreate):
    if user.age < 18:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User must be at least 18 years old'
        )
    return {
        'id': 1,
        'email': user.email,
        'age': user.age
    }

@router.put('/{user_id}', response_model=UserResponse)
def update_user(user_id: int, user: UserCreate):
    if user_id < 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user_id"
        )
    if user.age < 18:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User must be at least 18 years old'
        )
    
    return {
        'id': user_id,
        'email': user.email,
        'age': user.age
    }