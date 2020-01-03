#!/usr/bin/env python3

import telnetlib

class PyClient:

	def __init__(self, host, port):
		print("Initializing connection...")
		self.host = host
		self.port = port
		self.connection = None
		self.Connect()
		self.InitTCS()
		print("Connection ready")


	def Connect(self):
		try:
			self.connection = telnetlib.Telnet(self.host, self.port, 5)
		except:
			raise Exception("Could not establish connection")

	def InitTCS(self):
		if not self.connection:
			self.Connect()

		# Set TCS to nonverbose and select robot
		self.SendCommand("mode 0")
		self.SendCommand("selectrobot 1")

	def SendCommand(self, command):
		print(">> " + command)
		self.connection.write((command.encode("ascii") + b"\n"))
		response = self.connection.read_until(b"\n").rstrip().decode("ascii")
		if response[0] == "-":
			raise Exception("TCS error: " + response)

		print("<< " + response)
		return response


	def Close(self):
		self.connection.close()