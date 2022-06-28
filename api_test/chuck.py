# https://api.chucknorris.io/

import requests

url ='https://api.chucknorris.io/jokes/random'

result = requests.get(url)
result.encoding = 'utf-8'
# print('state cod :'+str(result.status_code))
if result.status_code == 200:
    print('Its all right')
else:
    print('Error connecting')

# assert 200 == result.status_code, 'Wrong state code'
print(result.text)
