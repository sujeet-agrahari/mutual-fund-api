from sqlalchemy.orm import Session
from mutual_fund_brokerage_api import schema
import bcrypt
from mutual_fund_brokerage_api.model import User


def register(user: schema.UserRegister, db: Session):
    new_user = User(
        email=user.email,
        password=hash_password(user.password),
        username=user.username,
        full_name=user.full_name,
    )
    db.add(new_user)
    db.commit()
    new_user_dict = new_user.__dict__.copy()
    new_user_dict.pop("password", None)
    return new_user_dict


def login(db: Session, user: schema.UserLogin):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user and verify_password(user.password, db_user.password):
        user_dict = db_user.__dict__.copy()
        user_dict.pop("password", None)
        return user_dict
    else:
        return {"error": "Invalid email or password"}


def hash_password(password: str) -> str:
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )

