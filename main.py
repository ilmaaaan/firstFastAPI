from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
from schemas import User

app = FastAPI(title = "Trading App")


@app.get("/")
def hello():
    return "Hello world!"


fake_users= [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
    {"id": 4, "role": "investor", "name": "Homer", "degree": [
        {"id": 1, "created_at": "2023-01-01T00:00:00", "type_degree": "expert"}
    ]}
]




@app.get("/users/{user_id}", response_model= List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]


fake_trades = [
    {"id":1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id":2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12}
]

@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 1):
    return fake_trades[offset:][:limit]


fake_users2= [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"}
]


@app.post("/users/{user_id}", response_model= List[User])
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id")==user_id, fake_users2))[0]
    current_user["name"]= new_name
    return {"status": 200, "data": current_user}


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge = 0)
    amount: float


@app.post("/trades")
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}
