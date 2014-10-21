import wiiuse
import serial
import time

def handle_event(wmp):
    wm = wmp[0]
    if wm.btns:
        if wiiuse.is_just_pressed(wm, wiiuse.button['-']):
            wiiuse.motion_sensing(wmp, 0)
        if wiiuse.is_just_pressed(wm, wiiuse.button['A']):
            wiiuse.motion_sensing(wmp, 1)
        if wiiuse.is_just_pressed(wm, wiiuse.button['B']):
            wiiuse.toggle_rumble(wmp)       
	return wm.orient.pitch
    
wiimotes = wiiuse.init(1)
found = wiiuse.find(wiimotes, 1, 5)
wiiuse.set_leds(wiimotes[0], wiiuse.LED[0])
if not found:
    print 'not found'
connected = wiiuse.connect(wiimotes, 1)
if connected:
	s = serial.Serial(7)		# COM7 virtual
	s.baudrate = 9600
	s.timeout = 0		# no espera a leer
	print " sa"
	while 1:
		r = wiiuse.poll(wiimotes, 1)	
		if r != 0:
			s.write(str(handle_event(wiimotes[0])))
			time.sleep(.005)
			print handle_event(wiimotes[0])	


