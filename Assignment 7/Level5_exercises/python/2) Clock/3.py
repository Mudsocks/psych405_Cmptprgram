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
end_text = visual.TextStim(win, text="This is the end of the trial!")

stims = ['face01.jpg','face02.jpg','face03.jpg'] #create a list if images to show
nTrials=3 #create a number of trials for your images

countdown_timer = core.CountdownTimer()
clock_wait_timer = core.Clock() #define a clock

for trial in range(nTrials): #loop through trials
    #-draw fixation
    fix_text.draw() #draw
    #-flip window
    win.flip() #show
    #-wait time (stimulus duration)
    core.wait(2)
    
    my_image.image = os.path.join(image_dir,stims[trial])

    countdown_timer.reset()
    countdown_timer.add(2)

    time_1 = clock_wait_timer.getTime() #get time on the clock

    while countdown_timer.getTime() >= 0: #since we go from -2 to 0
        my_image.draw() #draw
        win.flip() #show

    time_2 = clock_wait_timer.getTime() #get time on the clock

    final_time = time_2 - time_1
    print(final_time)

    #-draw end trial text
    end_text.draw() #draw
    #-flip window
    win.flip() #show
    #-wait time (stimulus duration)
    core.wait(2)
    
win.close() #close the window after trials have looped 