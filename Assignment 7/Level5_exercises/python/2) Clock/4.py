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

nBlocks=2
nTrials=3 #create a number of trials for your images

clock_wait_timer = core.Clock() #define a clock
block_timer = core.Clock()
trial_timer = core.Clock()
times = []
#=====================
#START TRIAL
#===================== 
for block in range(nBlocks):
    block_timer.reset()
        
    for trial in range(nTrials): #loop through trials
        trial_timer.reset()
        #-draw fixation
        fix_text.draw() #draw
        #-flip window
        win.flip() #show
        #-wait time (stimulus duration)
        core.wait(2)

        #-draw image
        my_image.image = os.path.join(image_dir,stims[trial])
        my_image.draw() #draw
        #-flip window
        win.flip() #show

        time_1 = clock_wait_timer.getTime() #get time on the clock
        #-wait time (stimulus duration)
        core.wait(2) #wait .5 seconds
        time_2 = clock_wait_timer.getTime() #get time on the clock

        final_time = time_2 - time_1
        times.append(final_time)

        #-draw end trial text
        end_text.draw() #draw
        #-flip window
        win.flip() #show
        #-wait time (stimulus duration)
        core.wait(2)

        print('Trial'+str(trial)+' time =', trial_timer.getTime()) #proper indent

    print('Block'+str(block)+' time =', block_timer.getTime()) #proper indent

print("Image times:")
print(times) #printed time was 1.999573899999632. Quite precise? To the 0.001
win.close()