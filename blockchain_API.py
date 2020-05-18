#
# Blockchain.info API Library
#
# Uses Blockchain.info's API to pull bitcoin blockchain data
# Note: Blockchain.info does not currently support bc1 addresses

VERSION=0.0

import requests
import datetime

def Get_Block_By_Hash(block_hash):
    url='http://blockchain.info/rawblock/{}?format=json'.format(block_hash)
    with requests.Session() as s:
        data=s.get(url).json()
    return data

def Get_Transaction_By_Hash(tx_hash):
    url='http://blockchain.info/rawtx/{}?format=json'.format(block_hash)
    with requests.Session() as s:
        data=s.get(url).json()
    return data

def Get_Single_Address_Info(address):
    url='http://blockchain.info/rawaddr/{}?format=json'.format(address)
    with requests.Session() as s:
        data=s.get(url).json()
    return data



