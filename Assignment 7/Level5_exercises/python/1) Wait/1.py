from psychopy import visual, monitors, event, core

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) #define a window

import os
#stuff you only have to define once at the top of your script
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')

fix_text = visual.TextStim(win, text='+')
my_image = visual.ImageStim(win)
end_text = visual.TextStim(win, text="This is the end of the experiment!")

stims = ['face01.jpg','face02.jpg','face03.jpg'] #create a list if images to show
nTrials=3 #create a number of trials for your images
        
#=====================
#START TRIAL
#===================== 
#-draw fixation
fix_text.draw() #draw
#-flip window
win.flip() #show
#-wait time (stimulus duration)
core.wait(2) #wait .5 seconds
        
#-draw image
my_image.image = os.path.join(image_dir,stims[1])
my_image.draw() #draw
#-flip window
win.flip() #show
#-wait time (stimulus duration)
core.wait(2) #wait .5 seconds
        
#-draw end trial text
end_text.draw() #draw
#-flip window
win.flip() #show
#-wait time (stimulus duration)
core.wait(2) #wait .5 seconds