#!/usr/bin/env python

# NAME    : IRC Server
# LICENSE : GNU General Public License
# DATE    : 2017-12-03
# VERSION : v0.1
# AUTHOR  : @joegalaxian
# NOTE    : Keep in mind, little to none logic on client side!

import logging
import select
import socket

from src import config
from src.clss.user import *

def init_logger():
	# Create logger
	logger = logging.getLogger('%s %s' % (config.name, config.version))
	logger.setLevel(logging.DEBUG)

	# Create file handler which logs even debug messages
	fh = logging.FileHandler(config.logfile)
	fh.setLevel(logging.DEBUG)

	# Create console handler with a higher log level
	ch = logging.StreamHandler()
	ch.setLevel(logging.INFO)

	# Create formatter and add it to the handlers
	formatter = logging.Formatter(config.logformat)
	fh.setFormatter(formatter)
	ch.setFormatter(formatter)

	# Add the handlers to the logger
	logger.addHandler(fh)
	logger.addHandler(ch)

	return logger

# Variables
server_socket = None
all_clients = []
unauth_clients = [] # new clients not yet authenticated/signedin

# Init logger
logger = init_logger()

# Init server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((config.host, config.port))
server_socket.listen(5)
logger.info('Server started at %s %s' % (config.host, config.port))

try:
	# Main loop
	while True:

		# Handle connections
		ready_to_read, ready_to_write, in_error = select.select(
			[server_socket] + all_clients
			, []
			, [server_socket] + all_clients # todo: how/when to use in_error?
		)

		for s in ready_to_read:

			# Handle new connetions
			if s == server_socket:
				client_socket, (client_host, client_port) = server_socket.accept()
				all_clients.append(client_socket)
				unauth_clients.append(client_socket)
				client_socket.send('Connected')
				logger.info('Client connected: %s %s' % (client_host, client_port))
				continue

			# Receive message
			msg = s.recv(config.block_size)
			cmd = msg.split()
			logger.info(cmd)

			# Handle disconnections
			if not msg:
				unauth_clients = [x for x in unauth_clients if x != s]
				all_clients = [x for x in all_clients if x != s]
				logger.info('Client disconnected')
				continue

			# Handle unauth clients
			if s in unauth_clients:

				# Signup: [ -u | --signup ] username [password]
				if cmd[0] in ('-u', '--signup'):
					if len(cmd) in (2, 3):
						user = User(
								cmd[1]
								, None if len(cmd) == 2 else cmd[2]
							)
						s.send('Signedup')
					else:
						s.send('Invalid call, try: [-u | --signup] username [password]')
					continue


				# Singin : [ -i | --signin ] username [password]
				elif cmd[0] in ('-i', '--signin'):
					if len(cmd) in (2, 3):
						pass
					else:
						s.send('Invalid call, try: [-i | --signin] username [password]')
					continue

				else:
					s.send('Unknown command')

			"""
			# Client's message
			elif s in all_clients:
				msg = s.recv(1024)

				# Client down
				if not msg:
					all_clients.remove(s)
					try: new_clients.remove(s)
					except: pass
					logger.info('Client disconnected')

				for c in all_clients:
					c.send(msg)

			else:
				pass # Not possible
			"""

except Exception as e:
	print e
	server_socket.close()
	print 'Program terminated.'
