from fastapi import FastAPI, Query
from typing import Optional
from mutual_fund_brokerage_api.db import get_db
from mutual_fund_brokerage_api.model import User
from mutual_fund_brokerage_api.services.auth import register, login
from mutual_fund_brokerage_api import model
from mutual_fund_brokerage_api.db import engine
from mutual_fund_brokerage_api import schema
model.Base.metadata.create_all(bind=engine)
from sqlalchemy.orm import Session
from fastapi import Depends
from mutual_fund_brokerage_api.services.mutual_fund import get_mutual_funds

app = FastAPI()

@app.post("/register")
def register_user(user: schema.UserRegister, db: Session = Depends(get_db)):
    return register(user, db)

@app.post("/login")
def login_user(user: schema.UserLogin, db: Session = Depends(get_db)):
    return login(db, user)


@app.get("/mutual-funds")
def get_funds(
    scheme_type: Optional[str] = Query(
        None, description="Type of mutual fund (Equity, Debt, Hybrid)"
    ),
):
    return get_mutual_funds(scheme_type)
