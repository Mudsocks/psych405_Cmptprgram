from psychopy import event, visual, monitors, core

mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

my_text = visual.TextStim(win)

nTrials=10

for trial in range(nTrials):
    my_text.text = "Please make a keypress for trial " + str(trial)
    my_text.draw()
    win.flip()
    core.wait(2)
    keys = event.getKeys()
    keys = event.clearEvents() #putting clearEvents before the print removes our inputs from keys which prints nothing to the console

if keys: #unindenting the if wont print out the key for each trial as it is not part of the loop, it will only print out the final trials keypress as that is the only value stored
    sub_resp = keys[0] #only count the first keypress
    print(sub_resp)
    
    
win.close()   