from web3 import Web3

class BlockchainReader:
    @staticmethod
    async def get_balance(
        *,
        wallet_address: str,
    ):
        provider_url = "https://mainnet.infura.io/v3/e44e8b13df9346a585df9bdf7b9d8bba"
        w3 = Web3(Web3.HTTPProvider(provider_url))

        if not w3.is_address(wallet_address):
            return "Invalid wallet address"

        balance = w3.eth.get_balance(wallet_address)
        
        balance_ether = w3.from_wei(balance, 'ether')

        return f"{balance_ether} ETH"
