import time
import requests

logPath = "Projekt\pozivnikLog.log"

botToken = "6587573197:AAHSv0fgkpDh_unOxNOe9UDXLb7Sq5hJOm8"
chatId = '6416443006'

with open(logPath, "rb") as f:
        Data = f.read()

logData = Data.decode('unicode_escape').split("\r\n")
lastMsg = logData[len(logData)-2]

url = f"https://api.telegram.org/bot{botToken}/sendMessage?chat_id={chatId}&text={lastMsg}"


while True:
    with open(logPath, "rb") as f:
        Data = f.read()

    logData = Data.decode('unicode_escape').split("\r\n")

    if (logData[len(logData)-2] != lastMsg):
        lastMsg = logData[len(logData)-2]
        print(requests.get(url).json())        
        print(lastMsg)
    

    time.sleep(0.1)

