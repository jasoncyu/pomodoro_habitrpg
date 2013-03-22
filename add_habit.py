#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
API_USER = '' 
API_KEY = ''

import sys
import json
import requests

task = sys.argv[1]

headers = {'content-type': 'application/json',
           'x-api-user': API_USER,
           'x-api-key': API_KEY}
payload = {"text": task, "type":"todo"}

r = requests.post('https://habitrpg.com/api/v1/user/task', data=json.dumps(payload), headers=headers)

