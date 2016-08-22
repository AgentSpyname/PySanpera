# PySanpera

##Intro
PySanpera is a collection of Python modules and scripts for interfacing with the Peavy Vyper Series of Amps. It was designed to use the same MIDI Commands that the offical Sanpera pedal does! The scripts can be used to build your own programs for custom footcontrollers, etc. Keep in mind that some scripts won't make sense to use stand-alone. **You will most likely have to make modifications and add some hardware to make it practical.** 

## License 
See LICENSE. 

##Requirements
* Python 3.5 and Pip3 or Higher
* python-rtmidi
* Peavey Vyper Amp that supports the Sanpera Pedal (Tested on VIP-1)
* MIDI-USB Interface or USB Type-A to USB-Type B Cable


## A Word On Installation
If you are using Mac OSX, it is suggested that you install Python3 using [Homebrew](http://www.brew.sh). On Windows, Google is your best friend, but as long as you get Python3 and Pip3 working you should be fine. On Linux. the version of pip3 in Yum or apt-get might be out of date, so make sure you install Python 3.5 with the correct version of Pip. **Above all, the main thing is to have Python 3 and the right version of Pip3 installed.**


##Usage
There a few directories with scripts in this project:

 - **Looper** - looper --> Contains the code with a basic program to control the onboard looper, with start/stop, and reset. 
 - **Presets** - preset_change --> Contains code to cycle between Presets 1-12 on your amp. 

### Future Additions

 - **Stompbox** - Ability to change the selected Stomp
 - **Reverb/Delay Control **
 - **Tap Tempo**
 - **Wah Wah** - Ability to control Wah. 
 - **Volume ** - Ability to change the amp volume(pedal)
 - **Extra Presets ** - Ability to use up to the 412 presets. 

