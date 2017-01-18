import requests

payload = {
    'email': 'something',
    'password': 'something'
    }

import sys

with requests.Session(config = {'verbose': sys.stderr}) as c:
    c.post('https://www.facebook.com/', data=payload)
    r = c.get('https://www.facebook.com/')
    print('sopier' in r.content)
