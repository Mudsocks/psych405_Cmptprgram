#1 it stretches the images by the same factor for both x and y

from psychopy import monitors, visual, event
import numpy as np
import os
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define experiment start text unsing psychopy functions
strt_txt = "Welcome to the experiment!"

#-define block (start)/end text using psychopy functions
block_strt_txt= "Starting Block" 
block_end_txt= "Ending Block"

#-define the monitor settings using psychopy functions
myMon = monitors.Monitor('myMonitor, width=5')

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=myMon, color=['red'], size=(1280,720), units= None, fullscr=True)





#=====================
#START EXPERIMENT
#=====================
#-present start message text
start_text = visual.TextStim(win, text=strt_txt)

#-allow participant to begin experiment with button press
event.waitKeys(5)  
#=====================
#BLOCK SEQUENCE
#=====================
nBlocks= 4
imgs=['f1.jpg', 'f2.jpg', 'f3.jpg']
#-for loop for nBlocks
for Block in range(nBlocks):

    #-present block start message
    visual.TextStim(win, text=block_strt_txt)
    #-randomize order of trials here
    np.random.shuffle(imgs)
    
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
    for img in imgs:
        #-set stimuli and stimulus properties for the current trial
        
        main_dir = os.getcwd() 
        sub_dir = os.path.join(main_dir,'imgs', img)
        print(sub_dir)
        #=====================
        #START TRIAL
        #=====================  
        #-draw fixation
        fixation_string= "+"
        fixation_txt= visual.ImageStim(win, text =fixation_string)
        fixation_txt.draw()
         
        #-flip window
        win.flip()

        #-wait time (stimulus duration)
        event.waitKeys(5) 
        #-draw image
        my_img= visual.ImageStim(win, image=sub_dir,size=5)
        my_img.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        event.waitKeys(5) 
        
        #-draw end trial text
        start_text = visual.TextStim(win, text=block_end_txt)

        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        event.waitKeys(5) 
        
#======================
# END OF EXPERIMENT
#======================        
#-close window
win.close