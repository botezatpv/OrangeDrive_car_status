import requests

r = requests.get('http://104.154.26.64/gate?name=Andrey&id=1')

print(r.json)

r2 = requests.post('http://104.155.156.203/sendSMS(+79265342055).json', data={'Rawpostdata':'Heol%20wrold!!!'})
print('\n')
print('sent')