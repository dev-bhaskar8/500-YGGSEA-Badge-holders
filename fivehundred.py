from web3 import Web3
from web3.auto import w3 as w
import os
from dotenv import load_dotenv

load_dotenv()

# my_address = os.getenv("PUBLIC_KEY")
# private_key = os.getenv("PRIVATE_KEY")
# private_key = bytearray.fromhex(private_key.replace("0x", ""))

contract_address = "0x13935dDB4BD229B41134754abE3023e69D94E3c0"
contract_address = w.toChecksumAddress(contract_address)

abi = os.getenv("ABI")
w3 = Web3(Web3.HTTPProvider(os.getenv('URL')))

contract_instance = w3.eth.contract(address=contract_address, abi=abi)

for i in range(500):
  print(contract_instance.functions.ownerOf(i).call())

