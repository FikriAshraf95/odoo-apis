import odoorpc

# Prepare the connection to the server
odoo = odoorpc.ODOO('localhost', port=8001)

# Login
odoo.login('POS_RETAIL_TEST', 'admin', 'admin')

# New order
if 'sale.order' in odoo.env:
    Order = odoo.env['sale.order']
    Order.create({
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
            "name": "Sales Order OdooRPC",
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
    })

    print("Sale Order created ..")
