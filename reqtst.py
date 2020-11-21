import requests

#r = requests.get('https://reqres.in/api/users/2')
#json_data = r.json()
#print(json_data['data']['first_name'])
'''
payload = {'first': 'one', 'second': 'two'}
r = requests.get('https://pretty-printed-request-bin.herokuapp.com/tp6ecftp', params=payload)
'''
headers = {'my-token': '234234234234'}
r = requests.get('https://pretty-printed-request-bin.herokuapp.com/tp6ecftp', headers=headers)