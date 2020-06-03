import sys
import time

import ibmiotf.application # to install pip install ibmiotf

import ibmiotf.device



#Provide your IBM Watson Device Credentials

organization = "Org ID" #replace the ORG ID

deviceType = "Device Type"#replace the Device type wi

deviceId = "Device ID"#replace Device ID

authMethod = "token"

authToken = "authtoken" #Replace the authtoken



def myCommandCallback(cmd): # function for Callback

        print("Command received: %s" % cmd.data)

        if cmd.data['command']=='lighton':

                print("LIGHT ON IS RECEIVED")

                          

        elif cmd.data['command']=='lightoff':

                print("LIGHT OFF IS RECEIVED")

                

        if cmd.command == "setInterval":

                

                if 'interval' not in cmd.data:

                        print("Error - command is missing required information: 'interval'")

                else:

                        interval = cmd.data['interval']

        elif cmd.command == "print":

                if 'message' not in cmd.data:

                        print("Error - command is missing required information: 'message'")

                else:

                        output=cmd.data['message']

                        print(output)



try:

	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}

	deviceCli = ibmiotf.device.Client(deviceOptions)

	#..............................................

	

except Exception as e:

	print("Caught exception connecting device: %s" % str(e))

	sys.exit()



# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times

deviceCli.connect()



while True:

              

        deviceCli.commandCallback = myCommandCallback



# Disconnect the device and application from the cloud

deviceCli.disconnect()

