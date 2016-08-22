import rtmidi

#Creates a 
def setup(device):
	global midiout #Makes midiout global, so other functions can use it later
	midiout = rtmidi.MidiOut() #Creates an MIDI Out
	midiout.open_port(device) #Opens the specified MIDI Device
	

#Looper
def looper(): #Looper Play/Rec
	note_on = [0x90, 0x00, 112]
	midiout.send_message(note_on)#Sends Command

def looper_endmidi(): #End MIDI Code for Above
	note_off = [0x80, 0x00, 0]

def looper_reset(): #Looper Reset/Stop
	note_on = [0x90, 0x02, 112] 
	midiout.send_message(note_on) 

def looper_reset_endmidi(): #End MIDI Code for Above
	note_off = [0x80, 0x02, 0]