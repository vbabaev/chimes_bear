import time
import datetime
import phraseBuilder
import chimeBuilder

class Clock:
	"""Simple talkink clock"""
		
	def __init__(self, voice):
		self.date = datetime.datetime.fromtimestamp(time.time())
		self.voice = voice

	def do_chimes_bong(self):
		time = self.date.strftime("%H_")
		minutes = int(self.date.strftime("%M"))
		minutes = 10 * (minutes / 10)
		time += str(minutes)
		self.voice.play(chimeBuilder.ChimeBuilder(time))

	def do_definite_bong(self):
		time = self.date.strftime("%H_%M")
		self.voice.play(phraseBuilder.PhraseBuilder(time))
