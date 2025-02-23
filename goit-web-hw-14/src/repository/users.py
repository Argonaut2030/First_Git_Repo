from libgravatar import Gravatar
from sqlalchemy.orm import Session

from src.database.models import User
from src.schemas import UserModel


async def get_user_by_email(email: str, db: Session) -> User:
    return db.query(User).filter(User.email == email).first()

async def create_user(body: UserModel, db: Session) -> User:
    """Create a user from a body .

    Args:
        body (UserModel): [description]
        db (Session): [description]

    Returns:
        User: [description]
    """
    avatar = None
    try:
        g = Gravatar(body.email)
        avatar = g.get_image()
    except Exception as e:
        print(e)
    new_user = User(**body.dict(), avatar=avatar)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def update_token(user: User, token: str | None, db: Session) -> None:
    user.refresh_token = token
    db.commit()
    """Update a refresh token for a user .
    """
async def confirmed_email(email: str, db: Session) -> None:
    """Set the user s confirmed email .

    Args:
        email (str): [description]
        db (Session): [description]
    """
    user = await get_user_by_email(email, db)
    user.confirmed = True
    db.commit()

async def update_avatar(email, url: str, db: Session) -> User:
    """Update a user s avatar .

    Args:
        email ([type]): [description]
        url (str): [description]
        db (Session): [description]

    Returns:
        User: [description]
    """
    user = await get_user_by_email(email, db)
    user.avatar = url
    db.commit()
    return user

