#!/usr/bin/env python3

import sys
import time
import pa_pyclient

try:
	if len(sys.argv) != 3:
		raise Exception("Connection requires both host and port arguments")

	host = sys.argv[1]
	port = sys.argv[2]
	client = pa_pyclient.PyClient(host, port)

	print("Beginning example routine")

	# Enable high power if necessary
	is_hp = client.SendCommand("hp")
	if is_hp == "0 0":
		client.SendCommand("hp 1")
		time.sleep(5)

	# Attach the robot to this thread
	client.SendCommand("attach 1")

	# Home if necessary
	is_homed = client.SendCommand("pd 2800")
	if is_homed == "0 0":
		client.SendCommand("home")

	# Begin example routine
	client.SendCommand("moveoneaxis 1 300 1")
	client.SendCommand("moveoneaxis 1 100 1")
	client.SendCommand("moveoneaxis 1 300 1")
	client.SendCommand("waitforeom")
	client.SendCommand("attach 0")



except Exception as e:
	print(str(e))

finally:
	try:
		client.Close()
	except:
		pass