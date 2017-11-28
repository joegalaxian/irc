# chat.py :  Source code of class Chat.

import datetime

class Chat(object):
	def __init__(self, creator, body, to):
		now = str(datetime.datetime.now())
		self.creator = creator
		self.body = body
		self.to = to
		self.status = 'created'
		self.status_dt = now
		self.created_dt = now

	def read(self):
		now = str(datetime.datetime.now())
		self.status = 'read'
		self.status_dt = now
		return self.body
