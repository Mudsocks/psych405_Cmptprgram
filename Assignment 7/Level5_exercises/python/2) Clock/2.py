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
clock_wait_timer = core.Clock() #define a clock
times = []
#=====================
#START TRIAL
#===================== 

for trial in range(nTrials): #loop through trials
    #-draw fixation
    fix_text.draw() #draw
    #-flip window
    win.flip() #show
    #-wait time (stimulus duration)
    core.wait(2) #wait .5 seconds

    #-draw image
    my_image.image = os.path.join(image_dir,stims[trial])
    my_image.draw() #draw
    #-flip window
    win.flip() #show

    time_1 = clock_wait_timer.getTime() #get time on the clock
    #-wait time (stimulus duration)
    core.wait(2) #wait .5 seconds
    time_2 = clock_wait_timer.getTime() #get time on the clock

    #-draw end trial text
    end_text.draw() #draw
    #-flip window
    win.flip() #show
    #-wait time (stimulus duration)
    core.wait(2) #wait .5 seconds

    final_time = time_2 - time_1
    times.append(final_time)

print(times) #printed time was 1.999573899999632. Quite precise? To the 0.001
win.close() #close the window after trials have looped 