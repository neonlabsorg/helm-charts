from web3 import Web3

# ETH_RPC_URL = 'http://localhost:8545'
ETH_RPC_URL = 'https://go-eth.neoninfra.xyz'
NETWORK_ID = 22222


ACCOUNT1_ADDRESS = Web3.to_checksum_address("0x123463a4b065722e99115d6c222f267d9cabb524")
ACCOUNT2_ADDRESS = Web3.to_checksum_address("0x14dc79964da2c08b23698b3d3cc7ca32193d9955")
ACCOUNT1_PRIVATE_KEY = "0x2e0834786285daccd064ca17f1654f67b4aef298acbb82cef9ec422fb4975622"
ACCOUNT2_PRIVATE_KEY = "0x01492bb4030f9726fea707865434894e5270b51facc1bace8d701e5aa83962cf"

# Connect to the private network
web3 = Web3(Web3.HTTPProvider(ETH_RPC_URL))

# Check connection
if not web3.is_connected():
    raise Exception("Failed to connect to the Ethereum node")

# Set sender account
sender_address = ACCOUNT1_ADDRESS
sender_private_key = ACCOUNT1_PRIVATE_KEY

balance = web3.eth.get_balance(sender_address)
print(f"Sender balance: {web3.from_wei(balance, 'ether')} ETH")

# Set receiver account
receiver_address = ACCOUNT2_ADDRESS

# Set the amount to transfer (in Wei). For example, send 1 Ether (1 Ether = 10**18 Wei)
amount = web3.to_wei(1, 'ether')

# Get nonce for the sender
# nonce = web3.eth.get_transaction_count(sender_address, 'pending')
nonce = web3.eth.get_transaction_count(sender_address)
print(f'nonce: {nonce}')

# Create the transaction
transaction = {
    'to': receiver_address,
    'value': amount,
    'gas': 21000,
    'gasPrice': web3.to_wei('20', 'gwei'),
    'nonce': nonce,
    'chainId': NETWORK_ID  # Replace with your network ID, e.g., if you have a private network
}

# Sign the transaction with the sender's private key
signed_transaction = web3.eth.account.sign_transaction(transaction, sender_private_key)

# Send the signed transaction
tx_hash = web3.eth.send_raw_transaction(signed_transaction.raw_transaction)

# Print the transaction hash
print(f"Transaction sent with hash: {tx_hash.hex()}")