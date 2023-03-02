from packages.func import func

data='{"order": {"line_items": [{"variant_id": 44641714536760,"quantity": 1}],' \
       '"applied_discount": {"description": "Custom discount","value_type": "fixed_amount","value": "10.0",' \
       '"amount": "10.00","title": "Custom"},"customer": {"id": 6802264686904},"use_customer_default_address": true}}'

order=func("orders",data)
print(order.create_())
print(order.get_())
print(order.del_())
print(order.del_all())
print(order.put(5254995411256))