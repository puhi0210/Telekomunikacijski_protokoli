import requests
import json

# get block

node_url = "https://mainnet.infura.io/v3/0ab7667b9cec47bdaa94fa906dd8244e"
headers = {
    "Content_Type": "aplication/json"
}

def getBlock(node_url, headers):    
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": ["latest", True],
        "id": 0
    }

    response = requests.post(node_url, data = json.dumps(payload), headers = headers)

    if response.status_code == 200:
        block_data = response.json()
        print("Dobili smo blok.")
        with open("Laboratorijske_vaje/Vaja6/DATA/blockData.json", "w") as f:
            json.dump(block_data, f, indent = 4)
    else:
        print(f"ni ratal. error code: {response.status_code}")
    return block_data

# Drugi del

data = getBlock(node_url, headers).copy()

def countTxs(data):
    counter = 0

    for transaction in data["result"]["transactions"]:
        counter += 1

    return counter



print(f"Stevilo transakcij je: {countTxs(data)}")


# Obe funkciji

def main(node_url, headers):
    data = getBlock(node_url, headers).copy()
    return countTxs(data)

print(f"Stevilo tranzakvij: {main(node_url, headers)}")