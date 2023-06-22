from app.internals.blockchain_reader import BlockchainReader

class BlockchainService:
    @staticmethod
    async def get_balance(
        *,
        wallet_address: str,
    ) -> str:
        return await BlockchainReader.get_balance(wallet_address=wallet_address)
