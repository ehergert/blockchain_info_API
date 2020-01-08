
# Simple Mixer Output Guesser (smog)

import requests
import datetime


def GetBlock_Height(block_height):
    url='http://blockchain.info/block-height/{}?format=json'.format(block_height)
    with requests.Session() as s:
        data=s.get(url).json()
    return data   


print ('Simple Mixer Output Guesser started.')
print ('\n')

# Get target amount
targetAmt=float(input('Target Amount: '))

# Get minimum splits
minSplits=int(input('Minimum number of splits: '))

# Get maximum splits
maxSplits=int(input('Maximum number of splits: '))

# Get starting block
startBlock=int(input('Starting block: '))

# Get number of blocks
totalBlocks=int(input('Number of blocks to search: '))

# identify target range (99.5-99.6%)
lowerRange=float(input('Lower bound (0.0% to 100.0%): '))/100
upperRange=float(input('Upper bound (0.0% to 100.0%): '))/100

# identify minimum amount (low range divided by max splits)
minAmt=targetAmt*lowerRange/maxSplits

# identify maximum amount (high range divided by min splits)
maxAmt=targetAmt*upperRange/minSplits

print('Min: {}'.format(minAmt))
print('Max: {}'.format(maxAmt))

# Loop through getting block tx info and pulling amounts in range into a list
potentialOutputs=[]
outdata=[]
outCount=0
for i in range(startBlock, startBlock+totalBlocks):
    print('Fetching block {} ({} of {})'.format(i,i-startBlock+1,totalBlocks))
    data=GetBlock_Height(i)
    for j in range(0, len(data['blocks'][0]['tx'])):
        for k in range(0, len(data['blocks'][0]['tx'][j]['out'])):
            outCount+=1
            out_value=data['blocks'][0]['tx'][j]['out'][k]['value']*10**-8
            if out_value > minAmt and out_value < maxAmt:
                try:
                    out_addr=data['blocks'][0]['tx'][j]['out'][k]['addr']
                except:
                    out_addr='unknown'
                tx_hash=data['blocks'][0]['tx'][j]['hash']
                outdata=[out_addr, out_value, tx_hash]
                potentialOutputs.append(outdata)
                outdata=[]
print('Total outputs reviewed: {}'.format(outCount))
print('Total potential outputs: {}'.format(len(potentialOutputs)))

#temp writing to text file
with open(r'c:\Python\my_files\btc.csv', 'w') as f:
    for line in potentialOutputs:
        for item in line:
            f.write('{}, '.format(item))
        f.write('\n')
        

# sort list by output amount
# look for pattern of matching amounts between min and max splits
# save potential matches into a list for follow up.
