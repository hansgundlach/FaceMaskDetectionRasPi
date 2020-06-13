import os
import requests
url = 'http://192.168.0.31:8000'
data = open('0.jpg', 'rb').read()
r = requests.post(url,data=data)
print(r.content)
