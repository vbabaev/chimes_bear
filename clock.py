import time
import datetime

class Clock:
	"""Simple talkink clock"""
		
	def __init__(self, voice):
		self.date = datetime.datetime.fromtimestamp(time.time())
		self.voice = voice

	def do_hourly_bong(self):
		phrase = self.date.hour
		self.voice.setPhrase(phrase)
		self.voice.play()

	def do_definite_bong(self):
		phrase = self.date.strftime("%H_%M")
		self.voice.setPhrase(phrase)
		self.voice.play()

