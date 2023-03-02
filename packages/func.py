import requests
import json

class func:
	def __init__(self, eti, data = None, id = None, url = None):
		self.url = url
		self.header = {'x-shopify-access-token': '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',
		               'Content-Type': 'application/json'}
		self.data = str(data).replace("'", '"')
		self.eti = eti
		self.id = id

	def url_(sefl):
		url = "https://lotus-6973.myshopify.com/admin/api/2023-01/{0}.json".format(sefl.eti)
		return url

	def create_(self):
		url = func.url_(self)
		r = requests.post(url, headers = self.header, data = self.data)
		if r.status_code == 201:
			return json.loads(r.text)
		return r.status_code

	def get_(self, id = None):
		if id != None:
			url = "https://lotus-6973.myshopify.com/admin/api/2023-01/{0}/{1}.json".format(self.eti, self.id)

		url = func.url_(self)
		r = requests.get(url, headers = self.header)
		return json.loads(r.text)

	def put_(self,id):
		url = "https://lotus-6973.myshopify.com/admin/api/2023-01/{0}/{1}.json".format(self.eti,id)
		# print(self.data)
		r = requests.put(url, headers = self.header, data = self.data)
		if r.status_code == 200:
			return "Ok"
		return r.status_code

	def del_(self, id):
		url = "https://lotus-6973.myshopify.com/admin/api/2023-01/{0}/{1}.json".format(self.eti, id)
		r = requests.delete(url, headers = self.header)
		if r.status_code == 200:
			return "OK"
		return r.status_code

	def del_all(self):
		eti_ = func.get_(self)
		for x in eti_[self.eti]:
			r = func.del_(self, x['id'])
		return r
