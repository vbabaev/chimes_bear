import time
import datetime

class Clock:
	"""Simple talking clock"""
		
	def __init__(self):
		self.date = datetime.datetime.fromtimestamp(time.time())

	def do_hourly_bong(self):
		print self.date.hour
	def do_definite_bong(self):
		print self.date.strftime("%H_%M")

