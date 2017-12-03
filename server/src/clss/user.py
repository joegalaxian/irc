# user.py : Source code of class User.

import datetime
import hashlib

def save_user(user):
	with open('db/users.db', 'a') as f:
		f.write('%s %s' % (user.name, user.password_hash))

def valid_username(user):
	with open('db/users.db') as f:
		flines = [line.split for line in f.readlines()]
		for line in flines:
			if user.name == line[0]:
				return False
		return True

class User(object):
	def __init__(self, name, password):
		now = str(datetime.datetime.now())
		self.name = name
		self.password_hash = hashlib.sha256(password).hexdigest()
		self.created_at = now
		if valid_username(self):
			save_user(self)
		else:
			raise Exception

	def change_password(self, password, new_password):
		if self.password_hash == hashlib.sha256(password).hexdigest():
			self.password_hash = hashlib.sha256(new_password).hexdigest()

	def change_name(self, password, name):
		if self.password_hash == hashlib.sha256(password).hexdigest():
			self.name = name
