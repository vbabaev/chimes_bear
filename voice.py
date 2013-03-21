class Voice:
	
	def __init__(self, directory):
		self.rootDirectory = directory

	def setPhrase(self, phrase):
		self.phrase = phrase

	def play(self):
		print self.phrase