#preset_bank.py
#Written By: Alexander Parsan, Licensed Under The GPL v3.0(See the LICENSE file.)
#Program to toggle between preset 0(My electric) and preset 8(my acoustic) on my Peavy Vyper  Amp.

#This program requires Python 3 > , easygui 0.96 < and python-rtmidi. This will not work in Python 2.


import sys
import rtmidi
import easygui

#Setups Amp MIDI Output
midiout = rtmidi.MidiOut()
midiout.open_port(0)
available_ports = midiout.get_ports()

#Sends init command to check connection. 
program_change = [0xC0, 0x00, 112] 
midiout.send_message(program_change)

easygui.msgbox("Connection established with " + available_ports[0])

#Main Program
while True:
	selection =  easygui.buttonbox(msg='Select either the Acoustic or Electric preset.', title='Preset Switcher', choices=('Acoustic', 'Electric', 'Quit'))

	if selection == 'Acoustic':
		program_change = [0xC0, 0x08, 112] 
		midiout.send_message(program_change)
	elif selection == 'Electric':
		program_change = [0xC0, 0x00, 112] 
		midiout.send_message(program_change)
	elif selection == 'Quit':
		del midiout
		sys.exit()

