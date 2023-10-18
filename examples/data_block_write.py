import requests

r = requests.post("http://127.0.0.1:1234/iota/message", json={"message": "value"})
print(r.text)
