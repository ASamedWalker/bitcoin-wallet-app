#!/usr/bin/env python

"""
Title - Get Trade Volume
This program demonstrates how to get the trade volume
of Bitcoin in various currencies using the
blockchain library.
"""

# import blockchain library
from blockchain import exchangerates, statistics

# get the stats object
stats = statistics.get()

# get the trade volume in various currencies
print(f"Bitcoin Trade Volume in various currencies: {stats.trade_volume_btc}")


# get and print Bitcoin mined
print(f"Bitcoin Mined: {stats.btc_mined}")


# get and print Bitcoin market price in USD
print(f"Bitcoin Market Price in USD: {stats.market_price_usd}")

# Find a block which moved the most bitcoins with a block height number of 916840
