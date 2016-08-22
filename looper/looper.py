import time
import sanpera

sanpera.setup(0)

while True:
	command = int(input("Press 1 to Turn On Looper, Press 2 to Turn Off Looper:"))

	if command == 1:
		time.sleep(4)
		sanpera.looper()

	if command == 2: 
		sanpera.looper_endmidi()
		sanpera.looper_reset()
		time.sleep(2)
		sanpera.looper_reset_endmidi()

