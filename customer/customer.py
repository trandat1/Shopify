from packages.func import func

data='{"customer": {"first_name": "Tran","last_name": "Dat","email": "GiaVien2002@gmail.com","phone": "0376508233","verified_email": true,"addresses": [{"address1": "Gia phuong","city": "Ninh Binh","province": "ON","phone": "0376508233","zip": "08300","last_name": "tran","first_name": "dat","country": "vn"}],"password": "","password_confirmation": "","send_email_welcome": false}}'
cus = func("customers",data,6802264686904)
# print(cus.create_())
print(cus.get_(6802264686904))
# cus.put_()