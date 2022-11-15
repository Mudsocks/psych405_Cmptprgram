
#1,
#2 Changing color space changes color of the window , yes we can define colors by name

from psychopy import monitors, visual, event



#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
myMon = monitors.Monitor('myMonitor, width=5')

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=myMon, color=['red'], size=(1280,720), units= None, fullscr=True)

event.waitKeys(5)  
win.close()