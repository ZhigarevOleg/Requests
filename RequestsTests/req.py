import requests

status = 'avaliable'

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?={status}', headers = {'accept':'application/json', 'Content-Type' : 'application/json'})   
 
print(res.status_code)
print(res.text)
print(res.json())


res = requests.post(f'https://petstore.swagger.io/v2/pet', headers = {'accept':'application/json', 'Content-Type' : 'application/json'}, json = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
                   
print(res.status_code)
print(res.text)
print(res.json())

res = requests.put(f'https://petstore.swagger.io/v2/pet', headers = {'accept':'application/json', 'Content-Type' : 'application/json'}, json = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})

print(res.status_code)
print(res.text)
print(res.json())

res = requests.delete(f'https://petstore.swagger.io/v2/pet/0', headers = {'accept':'application/json', 'Content-Type' : 'application/json'})

print(res.status_code)
print(res.text)


