# pa_pyclient
A very simple Python client to interact with TCS. More information on TCS can be found at Precise Automation's [software download page](http://preciseautomation.com/Support/LatestSoftwareUpdates.html).

This project contains two files:
* **pa_pyclient**:  
  This script contains the basic Telnet functionality used to establish communication with the robot.
  
* **example_script**:  
  This script provides an example of how to execute a series of commands. When executed, the robot will:
  1. Enable power (if not already enabled)
  2. Home (if not already homed)
  3. Move axis 1 up and down

To test the example,
1. Make sure the Tcp_cmd_server GPL project is running on the robot.
2. Make sure the example script is executable: `chmod +x example_script.py`
3. Run the example script with the robot's IP as the host and 10100 as the port number. For example,
`./example_script.py 192.168.0.1 10100`


---
*Permission is granted to customers of Precise Automation to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, so long as this notice is included with any modified or unmodified version of this software.*

*This software is provided "as is," without warranty of any kind, express or implied. In no event shall Precise Automation be held liable for any direct, indirect, incidental, special or consequential damages arising out of the use of or inability to use this software.*
