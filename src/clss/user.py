# user.py : Source code of class User.

import datetime
import hashlib

class User(object):
	def __init__(self, name, password):
		now = str(datetime.datetime.now())
		self.name = name
		self.password_hash = hashlib.sha256(password).hexdigest()
		self.created_at = now

	def change_password(self, password, new_password):
		if self.password_hash == hashlib.sha256(password).hexdigest():
			self.password_hash = hashlib.sha256(new_password).hexdigest()

	def change_name(self, password, name):
		if self.password_hash == hashlib.sha256(password).hexdigest():
			self.name = name
