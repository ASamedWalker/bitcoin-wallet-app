#!/usr/bin/env python

"""
Title - Bitcoin Blockchain API
This program demonstrates the usage of
- get_balance
- get_unspent
- history
functions from the bitcoin library.
"""

# import blockchain library
from blockchain import exchangerates, blockexplorer


# # get the bitcoin rates in various currencies
# ticker = exchangerates.get_ticker()
# print("Bitcoin Rates in various currencies:")
# for currency_code, currency_obj in ticker.items():
#     print(f"{currency_code}: {currency_obj.p15min}")


# # Getting Bitcoin value for a particular currency and amount
# btc = exchangerates.to_btc('USD', 100)
# print(f"\nValue of 100 USD in BTC: {btc}")


# Find a block which moved the most bitcoins with a block height number of 916840
try:
    blocks = blockexplorer.get_block_height(916840)
    if blocks:
      block = blocks[0]
      print("\nBlock at height 916840:")
      print(f"Block hash: {block.hash}")
      print(f"Number of transactions: {len(block.transactions)}")
    else:
      print("No blocks found at height 916840.")
except Exception as e:
    print(f"Error fetching block data: {e}")