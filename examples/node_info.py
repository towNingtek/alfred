import requests

r = requests.get('https://alfred.townway.com.tw/iota/info')
print(r.text)
