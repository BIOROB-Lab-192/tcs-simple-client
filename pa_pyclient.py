#!/usr/bin/env python3

import telnetlib

class PyClient:

	def __init__(self, host, port, mode = 0):
		print("Initializing connection...")
		self.host = host
		self.port = port
		self.mode = mode
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
		if self.mode == 0:
			# Set TCS to nonverbose
			self.SendCommand("mode 0")
		else:
			# Set TCS to verbose
			self.SendCommand("mode 1")
		self.SendCommand("selectrobot 1")

	def SendCommand(self, command):
		print(">> " + command)
		self.connection.write((command.encode("ascii") + b"\n"))
		if self.mode == 1:
			response1 = self.connection.read_until(b"\r\n").rstrip().decode("ascii")
		response2 = self.connection.read_until(b"\r\n").rstrip().decode("ascii")
		if response2 != "" and response2[0] == "-":
			raise Exception("TCS error: " + response2)
		print("<< "+ response2)
		return response2


	def Close(self):
		self.connection.close()
