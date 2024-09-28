from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from typing import Dict
import uvicorn

app = FastAPI()

transactions = []
payer_balances = {}

# Data Model for the transactions using BaseModel from PyDantic
class Transaction(BaseModel):
    payer: str
    points: int
    timestamp: str


@app.post("/add")
async def add(transaction: Transaction, response: Response):
    """
    Adds new transactions to the transaction dictionary.
    Updates the balance with points provided if user already
    in the dictionary. Return 200 status code if successful
    """
    transactions.append(transaction.dict())
    if transaction.payer not in payer_balances:
        payer_balances[transaction.payer] = 0
    payer_balances[transaction.payer] += transaction.points
    response.status_code = 200
    return response

class SpendPoint(BaseModel):
    points: int

@app.post("/spend")
async def spend(request: SpendPoint):
    """
    Takes a JSON request of the spent points. Points are subtracted in
    order of the oldest transactions. Raise error if points taken exceeds
    total points avaliable in the transaction dictionary.
    """
    points_requested = request.points
    points_total = sum(payer_balances.values())

    if points_requested > points_total:
        raise HTTPException(status_code=400, detail="Request amount greater than total available points")

    transactions.sort(key=lambda x: x['timestamp'])

    points_spent = []
    for transaction in transactions:
        if points_requested <= 0:
            break

        points_to_spend = min(transaction['points'], points_requested)
        transaction['points'] -= points_to_spend
        payer_balances[transaction['payer']] -= points_to_spend
        points_requested -= points_to_spend

        points_spent.append({'payer': transaction['payer'], 'points': -points_to_spend})

    transactions[:] = [t for t in transactions if t['points'] > 0]

    return {"points_spent": points_spent}

@app.get("/balance")
async def get_balance():
    """
    Returns the points for each payer and always return 200 status code.
    """
    return payer_balances
