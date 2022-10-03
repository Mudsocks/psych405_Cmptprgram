# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 19:47:23 2022

@author: ahmed
"""

# Python Tutorial: Level 1 Exercises

# Variable Operation Exercises

# 1
sub_code= 'sub'
subnr_int= 2
subnr_str= '2'

# 2
print(sub_code + " " + subnr_str)
print(sub_code + " " + subnr_str*3)
print((sub_code+subnr_str)*3)
print((sub_code*3)+(subnr_str*3))

# the (str) form of subnr can only be added to sub_code to get sub2 because you are adding to strings. subnr_int represents 2 as numerical data which can then perform mathematical operations


# List Operation Exercises


# 1
numlist= [1,2,3]
print(numlist*2)

# 2
import numpy as np
numarr=np.array([1,2,3])
print(numarr*2)

# Multiplying a list would simply repeat that same list(side by side) by the number being multiplied. While multiplying an array would multiply that number by each numerical value in the array

# 3
strlist= (['do','re','mi', 'fa'])

print([strlist[0]*2] + [strlist[1]*2] + [strlist[2]*2] + [strlist[3]*2])
print(strlist*2)
print(strlist[0:1]*2 + strlist[1:2]*2 + strlist[2:3]*2 + strlist[3:4]*2)
print([strlist[0:1]*2, strlist[1:2]*2, strlist[2:3]*2, strlist[3:4]*2])


#['dodo','rere','mimi','fafa']
#['do','re','mi','fa','do','re','mi','fa']
#['do','do','re','re','mi','mi','fa','fa']
#[['do','do'],['re','re'],['mi','mi'],['fa','fa']]


# Zipping Exercises

# 1

import numpy as np
first_list = []
second_list = []
imgs_house = ['house1.png']*5 + ['house2.png']*5 + ['house3.png']*5 + ['house4.png']*5 + ['house.png']*5                                                                      
imgs_face = ['face1.png']*5 + ['face2.png']*5 + ['face3.png']*5 + ['face4.png']*5 + ['face5.png']*5
cues = ['cue1']*50 + ['cue2']*50

first_list.extend(imgs_face)
first_list.extend(imgs_house)
first_list.extend(imgs_face)
first_list.extend(imgs_house)
img_fs = ['face1.png', 'face2.png', 'face3.png', 'face4.png', 'face5.png']*5                                                                
img_hs = ['house1.png', 'house2.png', 'house2.png', 'house3.png', 'house4.png', 'house5.png']*5

second_list.extend(img_hs)
second_list.extend(img_fs)
second_list.extend(img_hs)
second_list.extend(img_fs)

catimgs = list(zip(first_list, second_list, cues))

np.random.shuffle(catimgs)
print(catimgs)


# indexing Exercises

# 1

colors= ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# 2
print(colors[-1])


# 3
print(colors[-3:-5:-1])
    
# 4
colors.remove('purple')
colors.append('indigo')
colors.append('violet')
print(colors)


# Slicing Exercises

list100= list(range(0,101))
print(list100)
print(list100[:10])
print(list100[1:101:2][::-1])
print(list100[97:101][::-1])
