#!/usr/bin/env python

# NAME    : IRC Client Local
# LICENSE : GNU General Public License
# DATE    : 2017-12-03
# VERSION : v0.1
# AUTHOR  : @joegalaxian
# NOTE    : Keep in mind, little to none logic on client side!

import socket

connected = False
signedin = False
s = None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

while True:
	# Read command and ignore it, if empty.
	command = raw_input('> ')
	c = command.split()
	if not command:
		continue

	# Quit command : [ -q | --quit ]
	if c[0] in ('-q', '--quit'):
		if connected: s.send(command)
		if s: s.close()
		print 'Program terminated.'
		break

	if c[0] in ('-h', '--help'):
		# print help()
		pass

	if not connected:
		# Connect command : [ -c | --connect ] host port [password]
		if c[0] in ('-c', '--connect'):
			if len(c) not in (3, 4):
				print 'Invalid call, try: [ -c | --connect ] host port [passw ord]'
			else:
				host = c[1]
				port = int(c[2])
				s.connect((host, port))
				resp = s.recv(1024)
				print resp
				if resp == 'Connected':
					connected = True
				continue

	if connected:
		try:
			s.send(command)
			resp = s.recv(1024)
			print resp
		except socket.error:
			print 'Connection interrupted.\nProgram terminated.'
			break
