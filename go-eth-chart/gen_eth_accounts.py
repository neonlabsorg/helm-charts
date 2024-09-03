import json
from web3 import Web3


def generate_account():
    account = Web3().eth.account.create()
    return account


account1 = generate_account()
account2 = generate_account()

print("Account 1 Private Key:", account1._private_key.hex())
print("Account 1 Address:", account1.address)
print("Account 2 Private Key:", account2._private_key.hex())
print("Account 2 Address:", account2.address)

prefunded_accounts = {
    account1.address[2:]: {"balance": "1000000000000000000000000000000000000000000000000000000000"},
    account2.address[2:]: {"balance": "1000000000000000000000000000000000000000000000000000000000"}
}

output = json.dumps(prefunded_accounts, indent=2)[1:-1]
print(output)