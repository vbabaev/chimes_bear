import json
import os

class Config:
	def __init__(self):
		directory = os.path.dirname(os.path.realpath(__file__))
		data = open(directory + '/config.json', 'r')
		self.data = json.load(data)
	def get(self, key):
		return self.data[key]