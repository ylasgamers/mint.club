from web3 import Web3, HTTPProvider
import time
import datetime 
import json
import requests

#you can find rpc on chainlist.org or thirdweb.com/chainlist
web3 = Web3(Web3.HTTPProvider("https://nitrorpc-degen-mainnet-1.t.conduit.xyz"))
chainId = 666666666

#connecting web3
if  web3.is_connected() == True:
    print("Web3 Connected...\n")
else :
    print("Error Connecting Please Try Again...")

#choose chain you want to enabled, pick only one
#degen
merkleaddr = web3.to_checksum_address("0x5DaE94e149CF2112Ec625D46670047814aA9aC2a")
#base / arbitrum / bsc or bnb / ethereum / optimistic / polygon
#merkleaddr = web3.to_checksum_address("0x1349a9ddee26fe16d0d44e35b3cb9b0ca18213a4")
#avalanche
#merkleaddr = web3.to_checksum_address("0x841A2bD2fc97DCB865b4Ddb352540148Bad2dB09")
#blast
#merkleaddr = web3.to_checksum_address("0x29b0E6D2C2884aEa3FB4CB5dD1C7002A8E10c724")
#klaytn / zora
#merkleaddr = web3.to_checksum_address("0x3bc6b601196752497a68b2625db4f2205c3b150b")
#sepolia
#merkleaddr = web3.to_checksum_address("0x0CD940395566d509168977Cf10E5296302efA57A")

abi = json.loads('[{"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"AddressEmptyCode","type":"error"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"AddressInsufficientBalance","type":"error"},{"inputs":[],"name":"FailedInnerCall","type":"error"},{"inputs":[],"name":"MerkleDistributor__AlreadyClaimed","type":"error"},{"inputs":[],"name":"MerkleDistributor__AlreadyRefunded","type":"error"},{"inputs":[],"name":"MerkleDistributor__Finished","type":"error"},{"inputs":[],"name":"MerkleDistributor__InvalidCaller","type":"error"},{"inputs":[],"name":"MerkleDistributor__InvalidPaginationParameters","type":"error"},{"inputs":[{"internalType":"string","name":"param","type":"string"}],"name":"MerkleDistributor__InvalidParams","type":"error"},{"inputs":[],"name":"MerkleDistributor__InvalidProof","type":"error"},{"inputs":[],"name":"MerkleDistributor__NoClaimableTokensLeft","type":"error"},{"inputs":[],"name":"MerkleDistributor__NotStarted","type":"error"},{"inputs":[],"name":"MerkleDistributor__NothingToRefund","type":"error"},{"inputs":[],"name":"MerkleDistributor__PermissionDenied","type":"error"},{"inputs":[],"name":"MerkleDistributor__Refunded","type":"error"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"SafeERC20FailedOperation","type":"error"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"distributionId","type":"uint256"},{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Claimed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"distributionId","type":"uint256"},{"indexed":true,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"bool","name":"isERC20","type":"bool"},{"indexed":false,"internalType":"uint40","name":"startTime","type":"uint40"}],"name":"Created","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"distributionId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Refunded","type":"event"},{"inputs":[{"internalType":"uint256","name":"distributionId","type":"uint256"},{"internalType":"bytes32[]","name":"merkleProof","type":"bytes32[]"}],"name":"claim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"bool","name":"isERC20","type":"bool"},{"internalType":"uint176","name":"amountPerClaim","type":"uint176"},{"internalType":"uint40","name":"walletCount","type":"uint40"},{"internalType":"uint40","name":"startTime","type":"uint40"},{"internalType":"uint40","name":"endTime","type":"uint40"},{"internalType":"bytes32","name":"merkleRoot","type":"bytes32"},{"internalType":"string","name":"title","type":"string"},{"internalType":"string","name":"ipfsCID","type":"string"}],"name":"createDistribution","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"distributionCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"distributions","outputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"bool","name":"isERC20","type":"bool"},{"internalType":"uint40","name":"walletCount","type":"uint40"},{"internalType":"uint40","name":"claimedCount","type":"uint40"},{"internalType":"uint176","name":"amountPerClaim","type":"uint176"},{"internalType":"uint40","name":"startTime","type":"uint40"},{"internalType":"uint40","name":"endTime","type":"uint40"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint40","name":"refundedAt","type":"uint40"},{"internalType":"bytes32","name":"merkleRoot","type":"bytes32"},{"internalType":"string","name":"title","type":"string"},{"internalType":"string","name":"ipfsCID","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"distributionId","type":"uint256"}],"name":"getAmountClaimed","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"distributionId","type":"uint256"}],"name":"getAmountLeft","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"start","type":"uint256"},{"internalType":"uint256","name":"stop","type":"uint256"}],"name":"getDistributionIdsByOwner","outputs":[{"internalType":"uint256[]","name":"ids","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"start","type":"uint256"},{"internalType":"uint256","name":"stop","type":"uint256"}],"name":"getDistributionIdsByToken","outputs":[{"internalType":"uint256[]","name":"ids","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"distributionId","type":"uint256"},{"internalType":"address","name":"wallet","type":"address"}],"name":"isClaimed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"distributionId","type":"uint256"}],"name":"isWhitelistOnly","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"distributionId","type":"uint256"},{"internalType":"address","name":"wallet","type":"address"},{"internalType":"bytes32[]","name":"merkleProof","type":"bytes32[]"}],"name":"isWhitelisted","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bytes","name":"","type":"bytes"}],"name":"onERC1155Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"distributionId","type":"uint256"}],"name":"refund","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
contract = web3.eth.contract(address=merkleaddr, abi=abi)
numclaim = int(input("Input distributionId : "))

def MultiClaim(sender, pvkey):
    #estimate gas limit contract
    gas_tx = contract.functions.claim(numclaim, []).build_transaction({
        'chainId': chainId,
        'from': sender,
        'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
        'nonce': web3.eth.get_transaction_count(sender)
    })
    gasAmount = web3.eth.estimate_gas(gas_tx)

    #build a transaction in a dictionary
    claim_tx = contract.functions.claim(numclaim, []).build_transaction({
        'chainId': chainId,
        'from': sender,
        'gas': gasAmount,
        'gasPrice': web3.eth.gas_price, #web3.toWei(gasPrice,'gwei'),
        'nonce': web3.eth.get_transaction_count(sender)
    })

    #sign the transaction
    signed_tx = web3.eth.account.sign_transaction(claim_tx, pvkey)
    #send transaction
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

    #get transaction hash
    txid = str(web3.to_hex(tx_hash))
    print('')
    print('Transaction Success TX-ID')
    print(txid)
    
MultiClaim(web3.to_checksum_address("0xyouraddr1"), "yourpvkey1")    
MultiClaim(web3.to_checksum_address("0xyouraddr2"), "yourpvkey2")
