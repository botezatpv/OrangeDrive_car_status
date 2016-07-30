import requests

r = requests.get("http://104.154.26.64/gate?name=Andrey&id=1")

print(r.json)