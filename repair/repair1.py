#repair1.py - Script to troubleshoot broken control knobs on Peavy Vypyr VIP 1 Amps.  
#Written By: Alexander Parsan, Licensed Under The GPL v3.0(See the LICENSE file.)
#This program requires Python 3 and python-rtmidi. This will not work in Python 2.


import time
import rtmidi
import sys

print("This program will attempt to troubleshoot faulty knobs on the Peavey Vypyr Amp.")
#Checks for the Port.txt, opens or handles error
try:
	print (midiout.get_ports())
	port = int(input("Please enter the MIDI Port Number of your Vypyr: "))
except:
	print ("Invalid port. Auto selecting Port 0. ")
	port = "0"

#Creates an MIDI Output with the port
midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
midiout.open_port(int(port))

program_change = [0xC0, 0x00, 112] #Sends init command, check connection, fix bug. 
midiout.send_message(program_change)
print ("Connection established with " + available_ports[int(port)])

#Resets 
issue = int(input("What knob is giving trouble(Type 16 for pre gain, 17 for bass, 18 for mid, 19 for high, 22 for post gain): "))
program_change = [0xb0, issue, 0]  #Prepare command 
midiout.send_message(program_change) #Resets problem knobs to 0. 
print("The affected knob has been reset. Rerun this program to reset other knobs.")
