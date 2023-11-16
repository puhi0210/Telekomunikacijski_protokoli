import requests
import json

# Prvi del

# definiraj VARIABLE nase skripte
    # API URL od infure za Ethereum mainnet
node_url = "https://mainnet.infura.io/v3/0ab7667b9cec47bdaa94fa906dd8244e"

    # JSON-RPC request payload  (pogledamo dokumentacijo!)
payload = {
    "jsonrpc": "2.0",
    "method": "eth_getBlockByNumber",
    "params": ["latest", True],
    "id": 0
}

    # Nastavimo headerje za JSON-RPC request
headers = {
    "Content_Type": "aplication/json"
}

# Pošljemo request (uporabimo requests.post mdetodo)
response = requests.post(node_url, data = json.dumps(payload), headers = headers)

# Error handling. POgledamo če smo dobili pravilen odgovor.
    # ce ni error-ja (status code 200) sprintamo sporocilo in shranimo dobljeno sporocilo v json
if response.status_code == 200:
    block_data = response.json()
    print("Dobili smo blok.")
    with open("Laboratorijske_vaje/Vaja6/DATA/blockData.json", "w") as f:
        json.dump(block_data, f, indent = 4)
    # else, sprintaj sporocilo da nam ni uspelo dobiti zadnji block in dodaj kateri error oz. code-status code smo dobili
else:
    print(f"ni ratal. error code: {response.status_code}")

# Drugi del

# naredimo kopijo podatkov - .copy() metoda
data = block_data.copy()

# definiramo counter
counter = 0

# Iteriramo čez transakcije in povečujemo counter
for transaction in data["result"]["transactions"]:
    counter += 1
print(f"Stevilo transakcij je: {counter}")

# Izpišemo/sprintamo counter (število transakcij)