#!/usr/bin/env python3

import sys
import time
import pa_pyclient

print("Beginning example routine")
try:
	if len(sys.argv) != 3:
		host = "10.251.163.61"
		port = 23
	else:
		host = sys.argv[1]
		port = sys.argv[2]

	client = pa_pyclient.PyClient(host, port)

	print("Beginning example routine")
	client.SendCommand("mode 0")
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
		print("is homed")
		client.SendCommand("home")
		
	# get verbose mode 1 to hopefully get more on errors
	client.SendCommand("mode 1")
	client.mode = 1
	# Begin example routine
	client.SendCommand("MoveC 1 -212 100 600 15 175.569 72.883 38")
	client.SendCommand("MoveC 1 162 200 400 15 175.569 72.883 38")
	client.SendCommand("waitforeom")
	client.SendCommand("attach 0")

except Exception as e:
	print(str(e))

finally:
	try:
		client.Close()
	except Exception as e:
		print(f"Attempt to close client failed: {e}")