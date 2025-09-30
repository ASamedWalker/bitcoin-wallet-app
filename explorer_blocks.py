#!/usr/bin/env python

"""
Title - Block Explorer
This program demonstrates how to explore blocks
and transactions using the blockchain library.
"""

# import blockchain library
from blockchain import blockexplorer

# get a particular block
block = blockexplorer.get_block("000000000000000000015878e1771dcf72d65b4b105a81e0e0151f5a7772e9b2")

print(f"Block Fee: {block.fee}")
print(f"Block Size: {block.size}")
print(f"Block transactions: {len(block.transactions)}")


# get the latest block
latest_block = blockexplorer.get_latest_block()
print(f"\nLatest Block Height: {latest_block.height}")
