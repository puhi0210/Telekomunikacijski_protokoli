import requests
TOKEN = "6587573197:AAHSv0fgkpDh_unOxNOe9UDXLb7Sq5hJOm8"
chat_id = "6416443006"
message = "hello from your telegram bot"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json()) # this sends the message