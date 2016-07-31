import requests
import json

r = requests.get('http://104.154.26.64/gate?name=Andrey&id=1')

print(r.text)

r2 = requests.post('http://104.155.156.203/sendSMS(+79265342055).json', data={'Rawpostdata':'Heol%20wrold!!!'})
print('\n')
print(r2.text)
r3 = requests.request('POST','http://104.155.156.203/sendSMS(+79265342055).json?Rawpostdata=Heol%20wrold!!!')
print(r3.text)


response = requests.get('http://orangedrive.ru/gate?rq=open_car&user_id=1&lat=33&lng=35')
json_data = json.loads(response.text)
