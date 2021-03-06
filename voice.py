# -*- coding: utf-8 -*-

import os
import random
import subprocess


class Voice:

	directory = 'voice'
	ext = '.mp3'
	exceptionDirectories = ['.git']
	
	def __init__(self, directory, chimes):
		self.loadList(directory, chimes)

	def loadList(self, directory, chimes):
		directory = directory + Voice.directory
		if chimes:
			directory += '/chimes'
		else:
			directory += '/clock'
		self.voices = []
		pathes = os.listdir(directory)
		for name in pathes:
			path = directory + '/' + name
			if os.path.isdir(path) and path not in Voice.exceptionDirectories:
				self.voices.append({'name' : name, 'directory' : path})

	def getRandomVoice(self):
		return self.voices[random.randint(0, len(self.voices)) - 1]

	def play(self, phrase):
		""" я хуй его знает, как тут проиграть музыка, поэтому будет шелл вызов mpg123 """
		directory = self.getRandomVoice()['directory']

		audioFiles = []
		for file in phrase.getFiles():
			audioFile = directory + '/' + file + Voice.ext
			try:
				with open(audioFile): pass
			except IOError:
				raise
			audioFiles.append(audioFile)
		callParams = ["mpg123"] + audioFiles
		subprocess.call(callParams, stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
