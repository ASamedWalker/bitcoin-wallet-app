#!/usr/bin/env python
"""
Title - Hello Bitcoin
This program demonstrates the creation of
- private key
- public key
- and a bitcoin address.
"""
# import bitcoin
from bitcoin import *

my_private_key = random_key()

print(f"Private Key: \n{my_private_key}")

# Generate the public key from the private key
my_public_key = privtopub(my_private_key)
print(f"Public Key: \n{my_public_key}")

# Generate a bitcoin address from the public key
my_bitcoin_address = pubtoaddr(my_public_key)
print(f"Bitcoin Address: \n{my_bitcoin_address}")
