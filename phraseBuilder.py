from pprint import pprint

class PhraseBuilder:
	
	def __init__(self, phrase):
		self.files = []
		phrase = self.parse(phrase)

		self.files.append(self.getHourFile(phrase['hour']))
		hourfile = self.decline(phrase['hour'], 'hour', 'hour2', 'hour3')
		self.files.append(self.getHourFile(hourfile))


	def parse(self, phrase):
		parts = str(phrase).split('_')
		result = {'hour' : parts[0]}
		if len(parts) > 1:
			result['minute'] = parts[1]
		return result
	def getFiles(self):
		return self.files

	def getHourFile(self, filename):
		return 'hour/' + str(filename) 

	def decline(self, number, wordOne, wordTwo, wordMany):
		number = int(number)
		lastDigit = number % 10
		penaltimateDigit = (number / 10) % 10

		if penaltimateDigit == 1 or lastDigit == 0 or lastDigit >= 5:
			return wordMany
		if lastDigit == 1:
			return wordOne
		return wordTwo
