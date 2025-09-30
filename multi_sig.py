#!/usr/bin/env python
"""
Title - Create multi-signature address

This program demonstrates the creation of
Multi-signature bitcoin address.
"""
# import bitcoin
from bitcoin import *
from bitcoin import random_key, privtopub, mk_multisig_script, scriptaddr

# Generate random private keys for 2 users
user1_private_key = random_key()
user2_private_key = random_key()
user3_private_key = random_key()

print(f"User 1 Private Key: \n{user1_private_key}")
print(f"User 2 Private Key: \n{user2_private_key}")
print(f"User 3 Private Key: \n{user3_private_key}")
print("\n")

# Generate public keys for all users
user1_public_key = privtopub(user1_private_key)
user2_public_key = privtopub(user2_private_key)
user3_public_key = privtopub(user3_private_key)

print(f"User 1 Public Key: \n{user1_public_key}")
print(f"User 2 Public Key: \n{user2_public_key}")
print(f"User 3 Public Key: \n{user3_public_key}")
print("\n")

# Create a multi-signature script
multisig_sig = mk_multisig_script(
    user1_public_key, user2_public_key, user3_public_key, 2, 3
)

# Get the multi-signature address
multisig_address = scriptaddr(multisig_sig)

print(f"Multi-signature Address: \n{multisig_address}")
