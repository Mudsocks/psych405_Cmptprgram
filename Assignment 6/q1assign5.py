from psychopy import gui         
from datetime import datetime

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness


exp_info = {'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 
            'gender':(), 'session':1}  
my_dlg = gui.DlgFromDict(dictionary=exp_info,title = "subject info", fixed= ["session"], 
                        order= ["session", "subject_nr", "age", "gender", "handedness"], show=False) 
print('All variables have been created! Now ready to show the dialog box!')
data=my_dlg.show()
print(data)

#get date and time

filename = datetime.now().strftime("%d.%m.%Y_%H.%M.%S")+".txt"


#-create a unique filename for the data
import os
main_dir = os.getcwd() 
sub_dir = os.path.join(main_dir,'sub_info') 
if(not os.path.exists(sub_dir)):
    os.mkdir(sub_dir)
f = open(filename, "x")
f.write(data)
print(my_dlg)