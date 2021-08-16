import json
import random
import urllib.request

HOST = 'localhost'
PORT = 8001
DB = 'POS_RETAIL_TEST'
USER = 'admin'
PASS = 'admin'

# Partner ID
#     "id": 7,
#     "name": "Fikri Ashraf"

def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
        "Content-Type":"application/json",
    })
    reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]

def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})

# log in the given database
url = "http://%s:%s/jsonrpc" % (HOST, PORT)
uid = call(url, "common", "login", DB, USER, PASS)

# create a new order

args = {
    "create_uid": uid,
    "partner_id": 7,
        "order_line":[
            [
                0,0,{
                    "product_id": 50,
                    "product_uom_qty": 1,
                    "qty_delivered": 0,
                    "qty_invoiced": 1,
                    "price_unit": 15.00
                }
            ]
        ],
        "state": "sale",
        "confirmation_date": "2021-02-13 08:43:23",
        "name": "Sales Order JSONRPC",
        "invoice_count": 1,
        "invoice_ids": [
            16
        ],
        "invoice_status": "invoiced",
        "amount_by_group": [
                            [
                    "Tax 15%",
                    0.0,
                    0.0,
                    "$ 0.00",
                    "$ 0.00",
                    1
                ]
            ]
}

order_id = call(url, "object", "execute", DB, uid, PASS, 'sale.order', 'create', args)
print("Sale Order created..")
