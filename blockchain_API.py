#
# Blockchain.info API Library
#
#

VERSION=0.0

import requests
import datetime

def GetBlock_Hash(block_hash):
    url='http://blockchain.info/rawblock/{}?format=json'.format(block_hash)
    with requests.Session() as s:
        data=s.get(url).json()
    return data
