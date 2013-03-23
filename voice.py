# -*- coding: utf-8 -*-

import os
import random
import subprocess


class Voice:

	directory = 'voice'
	ext = '.mp3'
	exceptionDirectories = ['.git']
	
	def __init__(self, directory):
		self.loadList(directory)

	def loadList(self, directory):
		directory = directory + Voice.directory
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
		for file in phrase.getFiles():
			audioFile = directory + '/' + file + Voice.ext

			#print audioFile
			subprocess.call(["mpg123", audioFile], stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
