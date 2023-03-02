from packages.func import func

data={
    "custom_collection": {
        "title": "IPods",
        "collects": [
            {
                "product_id": 8162473378104
            }
        ]
    }
}
data={
    "custom_collection":{
        "id":438579757368,
        "title":"Quan Nam"
    }
}
cc = func("custom_collections",data)
# print(cc.create_())
# print(cc.del_())
# print(cc.get_())
print(cc.put_(438579757368))
