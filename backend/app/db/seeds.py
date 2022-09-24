import asyncio
from curses.ascii import HT
import os
import asyncpg

from fastapi import HTTPException

from ..api.dependencies.database import get_repository

from ..models.domain.users import User
from ..models.schemas.users import UserInCreate
from .repositories.users import UsersRepository
from ..api.routes.authentication import register


from ..models.schemas.items import ItemInCreate
from .repositories.items import ItemsRepository
from ..api.routes.items.items_resource import create_new_item

from ..models.schemas.comments import CommentInCreate
from .repositories.comments import CommentsRepository
from ..api.routes.comments import create_comment_for_item

from ..core.config import get_app_settings

loop = asyncio.new_event_loop()
conn = loop.run_until_complete(asyncpg.connect(os.environ.get('DATABASE_URL')))
users_repo = get_repository(UsersRepository)(conn)
items_repo = get_repository(ItemsRepository)(conn)
comments_repo = get_repository(CommentsRepository)(conn)
appsettings = get_app_settings()


for i in range(100):
    item = ItemInCreate(title=f'Item_{i}',
                        description=f'Description_{i}', body=f'Body_{i}')
    user = UserInCreate(
        username=f'User_{i}', email=f'user{i}@seed.com', bio=f'Bio_{i}', password=f'Password_{i}')

    comment = CommentInCreate(
        body=f'Comment_{i}'
    )

    try:
        loop.run_until_complete(register(user, users_repo, settings=appsettings))
    except HTTPException:
        pass

    res = loop.run_until_complete(create_new_item(item, user, items_repo))
    item = res.item

    try:
        loop.run_until_complete(create_comment_for_item(
            comment, item, user, comments_repo))
    except HTTPException:
        pass
