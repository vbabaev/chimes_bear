from pprint import pprint

class PhraseBuilder:
	
	def __init__(self, phrase):
		self.files = []
		phrase = self.parse(phrase)
		hours = self.parseNumber(phrase['hour'], 'm')
		for file in hours:
			self.files.append(self.getNumberFile(file))	
		hourfile = self.decline(phrase['hour'], 'hour', 'hour2', 'hour3')
		self.files.append(self.getHourFile(hourfile))

		if 'minute' in phrase:
			minutes = self.parseNumber(phrase['minute'], 'f')
			for file in minutes:
				self.files.append(self.getNumberFile(file))
			minuteFile = self.decline(phrase['minute'], 'minute', 'minute2', 'minute3')
			self.files.append(self.getMinuteFile(minuteFile))


	def parse(self, phrase):
		parts = str(phrase).split('_')
		result = {'hour' : int(parts[0])}
		if len(parts) > 1:
			result['minute'] = parts[1]
		return result

	def parseNumber(self, number, type='m'):
		number = int(number)
		lastDigit = number % 10

		if number <= 19 or lastDigit == 0:
			if number == 1 or number == 2:
				return [str(number) + type]
			return [number]
		decade = number - number % 10
		if lastDigit == 1 or lastDigit == 2:
			lastDigit = str(lastDigit) + type
		return [decade, lastDigit]


	def getFiles(self):
		return self.files

	def getNumberFile(self, file):
		return 'number/' + str(file) 

	def getHourFile(self, file):
		return 'hour/' + str(file) 

	def getMinuteFile(self, file):
		return 'minute/' + str(file)

	
	def decline(self, number, wordOne, wordTwo, wordMany):
		number = int(number)
		lastDigit = number % 10
		penaltimateDigit = (number / 10) % 10

		if penaltimateDigit == 1 or lastDigit == 0 or lastDigit >= 5:
			return wordMany
		if lastDigit == 1:
			return wordOne
		return wordTwo
