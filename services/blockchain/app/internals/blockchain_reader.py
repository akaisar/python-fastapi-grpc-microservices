from web3 import Web3

class BlockchainReader:
    @staticmethod
    async def get_balance(
        *,
        wallet_address: str,
    ):
        # Connect to the blockchain network using an appropriate provider
        provider_url = "https://mainnet.infura.io/v3/e44e8b13df9346a585df9bdf7b9d8bba"
        w3 = Web3(Web3.HTTPProvider(provider_url))

        # Check if the wallet address is valid
        if not w3.is_address(wallet_address):
            return "Invalid wallet address"

        # Fetch the balance of the wallet address
        balance = w3.eth.get_balance(wallet_address)
        
        # Convert the balance from wei to ether
        balance_ether = w3.from_wei(balance, 'ether')

        return f"{balance_ether} ETH"
