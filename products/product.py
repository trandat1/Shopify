from packages.func import func

# data = {
# 	"product": {
# 		"title": "Quan thun",
# 		"body_html": "<strong>Good snowboard!</strong>",
# 		"vendor": "Seashop",
# 		"product_type": "Snowboard",
#
# 		"options": [
# 			{
# 				"name": "Color",
# 				"values": [
# 					"Den",
# 					"Trang"
# 				]
# 			},
# 			{
# 				"name": "Size",
# 				"values": [
# 					"XXL",
# 					"XL"
# 				]
# 			}
# 		]
# 	}
# }

# data = {
# 	"product": {
# 		"id": 8162541437240,
# 		"title": "Quan Thun",
# 		"variants": [
# 			{
# 				"id": 44641714536760,
# 				"price": "180000",
# 				"sku": "Updating the Product SKU",
# 				"title": "Den",
# 			}
# 		]
# 	}
# }

pro = func("products")
# print(pro.del_(8162406039864))
# print(pro.create_())
print(pro.get_())
# print(product.del_all())
# print(pro.put_(8162541437240))
