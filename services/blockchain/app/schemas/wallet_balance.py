from pydantic import BaseModel

class WalletBalanceResponseSchema(BaseModel):
    wallet_balance: str
