import wiiuse


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
if not found:
    print 'not found'
connected = wiiuse.connect(wiimotes, 1)
if connected:
	while True:
		r = wiiuse.poll(wiimotes, 1)	
		if r != 0:
			print handle_event(wiimotes[0])	


