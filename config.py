import json

class Config:
	def __init__(self):
		data = open('config.json', 'r')
		self.data = json.load(data)
	def get(self, key):
		return self.data[key]