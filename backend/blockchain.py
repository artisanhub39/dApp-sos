from web3 import Web3
import json
from config import GANACHE_URL, CONTRACT_ADDRESS

w3 = Web3(Web3.HTTPProvider(GANACHE_URL))

with open("../bike-security-dpp/build/contracts/BikeSecurity.json") as f:
    contract_json = json.load(f)

abi = contract_json["abi"]

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)

account = w3.eth.accounts[0]