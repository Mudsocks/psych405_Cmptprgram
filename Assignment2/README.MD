# Operation Exercises

#1
print(5/2)
print(5.0/2.0)
# My version of python outputted the same values for both statements

#2
print(14%3)
print(16%4)
print(15%10)
# The modular operator (%) gives the remainder after running the division statement. 
# For example in line 29, 10 goes into 15 once with a remainder of 5, hence the output being '5'

#3
print(2**3)
print(16//3)
print(-16//3)
# Operator ** applies the power/exponent rule. 
# While // runs division where the decimals are disregared and the whole number is outputted
# However, if one number is negative, floor division is taking place where the number is rounded away from 0.
# For example, a true result of -1.4 will be displayed as -2.

#4
print(5+4-3*2-15/3)
print(4-3*2**2+(9-4))
# Yes, python follows order of operations.


# Variable Exercises

#1
letter1= 'A'
letter2= 'h'
letter3= 'm'
letter4= 'e'
letter5= 'd'

# 2 Yes, when I run the code, the assigned letters show up in the variable editor

#3
letterX= 'A'
print(letterX)
print(letter1)
# No issues when 2 different variables have the same value as both were outputted

#5
letterX='F'
print(letterX)
# Changing the value of letterX in step 5 did not change the value of the other variable
 

#6
letterX=letter1
print(letterX, letter1)
letter1='z'
print(letterX,letter1)
# Changing letter1 did not change the value of letterX after making letter1=z. 
# This shows us that python variable assigment goes from top -> bottom 


# Boolean Exercises
#1
print(1==1.0)
print("1"=="1.0")
# i belive the first statement is just equating the numerical values are the equivalent. 
# But in the second line it is equating if the two strings between the quotes are the same, in which they aren't

#2
print(5 == (3+2))

#3
print (1==1.0 or "1"=="1.0" or 5==(3+2))
print (1==1.0 or "1"=="1.0" and 5==(3+2))
print (1==1.0 and not "1"=="1.0" or 5==(3+2))
print (1==1.0 and not "1"=="1.0" and 5==(3+2))
print (1==1.0 and not "1"=="1.0" or not 5==(3+2))


#List Exercises 

#1
oddlist=[1,3,5,7,9]
# oddlist did become a variable

#2
print(oddlist)

#3
print(len(oddlist))
# it shows 5, representing 5 numbers in the list

#4 
print(type(oddlist))
# They type of list is <class 'list'>

#5
intlist= list(range(101))
print(intlist)


# Dictionary Exercises 

#1
about_me= { 0 : 'Ahmed', 1: 21.0, 2: 5, 3: 'Steak and burgers'}
print(about_me)

#2
print(type(about_me))
# It shows up as <class 'dict'>

#3
print(len(about_me))
# Shows length of 4. It determines length by determining the number of 
# key-value pairs within the dictionary.

# Array Exercises
#1
import numpy as np
mixnums= np.array([1,4,9,2.0,5.0,6.0])
print(mixnums)
# This was the output ->[1. 4. 9. 2. 5. 6.]
# all numbers had a decimal but no number after 

#2
mixtypes= np.array([2,4,6.0,8.0,'A','Z'])
print(mixtypes)
# Everything came out as a string

#3
oddarray= np.arange (1,101,2)
print(oddarray)

#4
logarray=np.logspace(1,5,16)
print(logarray)
