# channel.py : Source code of class Channel

import datetime

class Channel(object):
	def __init__(self, name, creator):
		now = str(datetime.datetime.now())
		self.name = name
		self.creator = creator
		self.chats = []
		self.created_at = now

	def add_chat(self, chat):
		self.chats.append(chat)

	def read(self):
		return self.chats
