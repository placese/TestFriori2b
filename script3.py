import requests
import re

URL = 'http://jsonplaceholder.typicode.com/users'
patternNet = re.compile('.+\.net')
patternOrg = re.compile('.+\.org')

r = requests.get(URL)
response = r.json()
for i in response:
    # print(i['name'])
    if re.match(patternNet, i['email']) or re.match(patternOrg, i['email']):
        print(i['name'])
