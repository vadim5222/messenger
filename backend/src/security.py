from pwdlib import PasswordHash
from typing import List

from enum import Enum

from typing import Annotated

from fastapi import Depends, HTTPException, status


from users.models import User
from users.utils import get_active_current_user




password_hash = PasswordHash.recommended()



class UserRoles(str, Enum):
    admin = 'Admin'
    user = 'User'
    moderator = 'Moderator'


class RoleChecker:
    def __init__(self, allowed_roles: List[UserRoles]):
        self.allowed_roles = allowed_roles

    def __call__(self, user: Annotated[User, Depends(get_active_current_user)]):
        if user.role.title in self.allowed_roles:
            return {'access':'Доступ резрешен'}
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
        



def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password):
    return password_hash.hash(password)