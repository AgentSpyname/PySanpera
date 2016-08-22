#preset_bank.py
#Written By: Alexander Parsan, Licensed Under The GPL v3.0(See the LICENSE file.)
#Program to toggle between the face presets 1-12 on the Peavy Vyper 1 Amp.

#This program requires Python 3 and python-rtmidi. This will not work in Python 2.


import time
import rtmidi
import sys

#Checks for the Port.txt, opens or handles error
try:
	f = open("port.txt", 'r') #Opens the port.txt file
	port = f.read(1) #Reads the first byte; this is the port no.
	f.close()
except:
	print ("There is no file named port.txt. Auto-selecting Port 0.")
	port = "0"

#Creates an MIDI Output with the port
midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
midiout.open_port(int(port))

program_change = [0xC0, 0x00, 112] #Sends init command, check connection, fix bug. 
midiout.send_message(program_change)
print ("Connection established with " + available_ports[int(port)])

#Starts a loop to choose which preset.
while True:
	preset = input("Enter the preset 0-11 which you would like to change, 100 to quit:")
	
	#Checks if its a number or not.. 
	if preset.isnumeric():
		preset = int(preset) #Makes the number an int
		if preset == 100: #100 will gracefully remove the MIDI output and close the program.
			del midiout
			sys.exit()
		elif preset > 11: #Prevents you from hurting your ears by limmiting the control number. Learned the hard way.
			print ("That is not a valid preset number.")
		elif preset < 12: #If the number is safe, change!
			values = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x10, 0x11, 0x12] #Hex Values
			program_change = [0xC0, values[preset], 112] #Program Change command. Contains the program change, and the bank you are changing. 112 is a dummy value.
			midiout.send_message(program_change) #Changes the bank
			print ("Command sent to " +  available_ports[int(port)]) 
	else:
		print ("Please enter a preset between 1 and 12")

