from packages.func import func

def del_all():
	func("customers").del_all()
	func("products").del_all()
	func("orders").del_all()
	func("smart_collections").del_all()
	func("custom_collections").del_all()
