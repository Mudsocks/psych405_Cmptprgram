# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 19:30:19 2022

@author: ahmed
"""

#Level 2: Conditionals and Loops

#Conditional exercises

#

#1
responses= ['1','2']

for response in responses:
    
    if response =='1' or response =='2':
        print('OK')
  
    
response= 'NaN'    

if response=='NaN':
    print("Subject did not respond")

else: print('Subject pressed the wrong key')

#2

response= '1'

if response=='1':
    print('Correct!')
    
response='2'
if response == '2':
    print('Incorrect!')
else: print('Subject pressed the wrong key')

#3
#Yes, it does what I expect it to. For part 1 when i respond with either 1 or 2, I get an 'OK' message. If its left empty ("NaN"), i recieve "subject did not respond" message. Lastly, any other response I get "subject pressed the wrong key".
    

#For loop exercises

#1

name = 'Ahmed'
for letter in name:
    print(letter)
    
# 2. 
count = -1 

for letter in name: 
    count = count + 1
    
    letter_numbered = letter + " %i" % count
    print(letter_numbered)
    
#3
name_list = ['Amy','Rory','River']

for name in name_list:

    for lt in name:
      print(lt)
#4
for name in name_list:
    count = -1 

    for lt in name:
        count+=1
        print(lt,count)

#While loop exercises

#1

i = 0
while i < 20:
    i = i + 1
    
    if i < 11 :
        print('image1.png')
      
    if i>= 11:
        print('image2.png')
      
#2
import random
correct_resp = False 

while not correct_resp: 
    print('image.png')

    imput_resp = random.randint(0,10)
    if imput_resp == 1 or imput_resp == 2:
        correct_resp = True

#3
import random
correct_resp = False 
failsafe = 0 
iterations = 0 

while not correct_resp:
    iterations+=1
    print('Showing an image for %i iterations' %iterations)
    print('image.png')
      
    imput_resp = random.randint(0,10)
    if imput_resp == 1 or imput_resp == 2:
        correct_resp = True
      break
	
    failsafe = failsafe + 1
    if failsafe == 5:
      break 
