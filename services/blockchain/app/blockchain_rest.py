from decimal import Decimal

from fastapi import APIRouter, Depends, HTTPException, Path

from app.schemas.wallet_balance import WalletBalanceResponseSchema
from app.blockchain_service import BlockchainService
from app.api.deps import check_authic_auth_token

router = APIRouter()

@router.get("/balance/{wallet_address}/", response_model=WalletBalanceResponseSchema)
async def get_wallet_balance(
    wallet_address: str = Path(...),
    authorized: bool = Depends(check_authic_auth_token)
) -> WalletBalanceResponseSchema:
    if not authorized:
        raise HTTPException(status_code=401, detail="Unauthorized")
    wallet_balance = await BlockchainService.get_balance(wallet_address=wallet_address)
    if not wallet_balance:
        raise HTTPException(status_code=404, detail="Wallet does not exists!")
    return {
        'wallet_balance': wallet_balance
    }

@router.get("/greeting")
async def greeting() -> str:
    return "Hello, World"
