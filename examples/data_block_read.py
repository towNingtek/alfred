import requests

r = requests.get("https://alfred.townway.com.tw/iota/message/?messageID=0xbbce7a7541cdf639b7699da5577de0e2c9f8586d6364bbba4a43c2c45e017b9c")
print(r.text)
