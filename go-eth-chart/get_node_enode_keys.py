import os
from eth_keys import keys

# Generate random bytes for the private key (32 bytes)
node_private_key_bytes = os.urandom(32)

# Create a private key from bytes
node_private_key = keys.PrivateKey(node_private_key_bytes)
node_public_key = node_private_key.public_key

# Generate ENODE from the public key
enode = node_public_key.to_bytes()

# Convert private key bytes to hex without '0x'
node_private_key_hex = node_private_key_bytes.hex()
node_public_key_hex = enode.hex()

print('NODE_KEY_HEX:', node_private_key_hex)
print('ENODE:', node_public_key_hex)