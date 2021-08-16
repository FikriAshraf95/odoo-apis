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

# Authenticate user
res = requests.post(
    AUTH_URL,
    data=json.dumps(data),
    headers=headers
)

# Get session_id from the response cookies
# We are going to use this as our API key
session_id = res.cookies.get('session_id', '')
print(session_id)


# Example 1
# Get users
USERS_URL = 'http://localhost:8001/api/res.users/'

# Pass session_id for auth
# This will take time since it retrives all res.users fields
# You can use query param to fetch specific fields
params = {'session_id': session_id}

res = requests.get(
    USERS_URL,
    params=params
)

# This will be a very long response since it has many data
print(res.text)


# Example 2
# Get products(assuming you have products in you db)
# Here am using query param to fetch only product id and name(This will be faster)
USERS_URL = 'http://localhost:8001/api/product.product/'

# Pass session_id for auth
params = {'session_id': session_id, 'query': '{id, name}'}

res = requests.get(
    USERS_URL,
    params=params
)

# This will be small since we've retrieved only id and name
print(res.text)
