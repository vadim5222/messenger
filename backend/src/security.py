from enum import Enum
from typing import Annotated, List

from fastapi import Depends, HTTPException, status
from pwdlib import PasswordHash
from users.models import User, Permissions
from users.utils import get_active_current_user, get_current_user_permissions

password_hash = PasswordHash.recommended()


class UserRoles(str, Enum):
    admin = "Admin"
    user = "User"
    moderator = "Moderator"



class UserPermissions(str, Enum):
    post_read = 'post:read'
    post_delete = 'post:delete'
    user_delete = 'users:delete'


class RoleChecker:
    def __init__(self, allowed_roles: List[UserRoles]):
        self.allowed_roles = allowed_roles

    def __call__(self, user: Annotated[User, Depends(get_active_current_user)]):
        if user.role.title in self.allowed_roles:
            return user
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)



# ===TODO: исправить логику проверки на права доступа
class PermissionChecker:
    def __init__(self, allowed_permissions: List[UserPermissions]):
        self.allowed_permissions = allowed_permissions

    async def __call__(self, permissions: Annotated[Permissions, Depends(get_current_user_permissions)]):
        for permission in permissions:
            if permission.title in self.allowed_permissions:
                return
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='У вас недостаточно прав'
        )




def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def get_password_hash(password):
    return password_hash.hash(password)
