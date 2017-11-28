#!/usr/bin/env python

# app.py : IRC application

from src.clss.user import User
from src.clss.chat import Chat
from src.clss.channel import Channel

if __name__ == '__main__':
	user = User('jose', 'pass')
	user2 = User('pepe', '1234')
	channel = Channel('#mychannel', user)
	chat = Chat(user, 'Hello world!', user2)
	print chat.read()
