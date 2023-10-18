import requests

r = requests.post("https://alfred.townway.com.tw/iota/message", json={"message": "hello"})
print(r.text)
