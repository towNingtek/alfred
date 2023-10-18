import requests

x = requests.get('http://127.0.0.1:1234/iota/info')
print(x.text)
