import json
import requests
import sys

AUTH_URL = 'http://localhost:8001/web/session/authenticate/'

headers = {'Content-type': 'application/json'}

# Remember to configure default db on odoo configuration file(dbfilter = ^db_name$)
# Authentication credentials
data = {
    'params': {
         'login': 'eefikri@gmail.com',
         'password': 'admin',
         'db': 'EA_attendance'
    }
}

# Authenticate user -------------------
response = requests.post(
    AUTH_URL,
    data=json.dumps(data),
    headers=headers
)

# print(response.text)
json_data = json.loads(response.text)
sessionID = json_data['result']['session_id']
print(sessionID)

# MORE SECURE WAY ---------------------
# cookies = response.cookies
# print(cookies)


# GET ----------------------------------
USERS_URL = 'http://localhost:8001/api/res.users/'

params = {'query': '{id, name}'}

response = requests.get(
    USERS_URL,
    params=params,
    cookies=cookies

)

# json_data = json.loads(response.text)

# print(json_data)
