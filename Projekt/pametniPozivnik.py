import time
import requests

logPath = "Projekt\pozivnikLog.log"     # Lokacija log datoteke

# Bot API token in ID kanala na katerega dobimo sporočilo
botToken = "BOT_TOKEN"
chatId = "CHAT_ID"

# Branje log datoteke
with open(logPath, "rb") as f:
        Data = f.read()

logData = Data.decode("unicode_escape").split("\r\n")   # Pretvorba iz bytes-like v string
lastMsg = logData[len(logData)-2]      # Shramba zadnjega sporočila (sporočilo je splitano tako da je zadnji element prazen, zato je -2 namesto -1)

url = f"https://api.telegram.org/bot{botToken}/sendMessage?chat_id={chatId}&text={lastMsg}"     # Generiranje HTTP poizvedbe


while True: # Neskončna zanka
    with open(logPath, "rb") as f:
        Data = f.read()

    logData = Data.decode('unicode_escape').split("\r\n")

    if (logData[len(logData)-2] != lastMsg): # Preverjanje zadnjega sporočila v log in shranjenega zadnjega sporočila 
        lastMsg = logData[len(logData)-2]
        print(requests.get(url).json())    # Pošiljanje poizvedbe    
        print(lastMsg)
    

    time.sleep(0.1) # Log datoteko preverimo vsakih 100ms

