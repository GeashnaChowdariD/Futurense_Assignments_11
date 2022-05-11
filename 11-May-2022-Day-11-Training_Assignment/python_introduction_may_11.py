#software
#compiler and interpreterr
#compiler
#interpreter or scripting or dynamic
#Runtime memory allocation - dynamic
#cpython
#Top down programming
#python runs their code in sequential way - GIL
#python memory works on the basis of Virtual memory concept
#python is automated garbage collectioon
#python open source
#library
#unstructured programming language
#object oriented programming
#forward compatabiility
#Task 1 --- version Comp
#Task 2 --- when we have different version of python how PIP
#Task 3 --- creating virtual environment

import random
'''
var = "dhoni"
var = var.replace("i","y")
print(var)
print(var[0])


var = "dhoni"

print(var[0:])

print(var[0:4])

print(var[2:0])

print(var[-2:0])

print(var[-2:-5])

print(var[0:-3])
print(var[::2])
print(var[::-2])
var = "dhoni msd"
print(dir(var))
var = 'dhoni'

var = "kohli"
var = "dhoni", 'msd'
var = "dhoni" 'csk'

var = "dhoni" 'csk'
var = "dhoni'csk"
##var = "dhoni plays
##fr csk"
var = "dhoni 'c'sk"
print(var)

var = """dhoni plays
 for csk"""
print(var)
var = """dhoni plays \
for csk"""
print(var)

var = """dhoni plays /
for csk"""
print(var)

var = list(input("enter the data").split())
print(var)
## r befor path

name = "dhoni"
age = 38
output = "my captain " + name+" plays even at the age of "+ str(age)
print(output)

name = "dhoni"
age = 38
output = "my captain %s plays even at the age of %d" %(name, age)
print(output)
name = "dhoni"
age = 38
output = "my captain {} plays even at the age of {}".format(name, age)
print(output)

name = "dhoni"
age = 38
output = f"my captain {name} plays even at the age of {age}"
print(output)

name = "dhoni plays for csk"
for x in name:
    print(x)


name = "dhoni plays for csk"
##__iter__(hold the state of the travelled letter)

for x in name:
    print(x, end=" ")
    #__next__

#__iter__ magic methods , d_methods
#__next__
#iter()
#generator()
name = "dhoni"
name1 = "kohli"

for x,y in zip(name,name1):
    print(x,y)


#name = "dhoni"
#name1 = "kohli"
#output = iter(name, name1)
#print(output)

#name = ["dhoni"]
#name1 = ["kohli"]
#output = iter(name, name1)
#print(output)

name = "dhoni"
name1 = "kohli"
output = list(zip(iter(name, name1)))
print(output)

var = "dhoni is my captain"

for x in enumerate(var):
    print(x)
var = "dhoni is my captain"
for x, y in enumerate(var):
    print(x)
    print(y)

var = "dhoni is my captain"
for x, _ in enumerate(var):
    print(x)

var = "dhoni is my captain"
for x, y in enumerate(var):
    if x%2 == 0:
        print("success")

for x, y in enumerate(var):
    if y=="i" or y=="a":
        print("success"")


#difference between  range and xrange

for x in range(10):
    print(x)

for x in range(2,10):
    print(x)

#for x in range(2,10,-1):
    #print(x)

output=0

for x in range(10, 1, -1):
    #output = output - 1
    output -= 1
print(ouput)


import random
print(random.randrange(-5,-2))
print(random.randint(1,9)) #require two parameters
print(random.random())

from numpy import random

output = random.randint(25) #can be one or two parameters
print(output)

output = random.rand()
print(output)

'''
#curl, wget -- server to server
#shutil --copy(), copy2()
#os --- output = os.stat("hello.txt")
#subprocess
#sys, popen
# python -m http.server

# import shutil
# import os
# import time
# import stat
#
# file_src = "E:\Futurense_training_online\serial_io.py"
# file_dst = "E:\Futurense_training_online\Offline_training\Testing"
# output = shutil.copy2(file_src,file_dst)
# meta1 = os.stat(file_src)
#
# meta2 = os.stat(file_dst)
# print(meta1)
# print(meta2)
# print(output)
#
# accessTime = time.ctime ( meta1 [ stat.ST_CTIME ] )
# accessTime2 = time.ctime ( meta2 [ stat.ST_CTIME ] )
#
# print(accessTime)
# print(accessTime2)

# file_src = "E:\Futurense_training_online\serial_io.py"
# file_dst = "E:\Futurense_training_online\Offline_training\Testing"
# output = shutil.copy2(file_src,file_dst)
# meta1 = os.stat(file_src)
# meta2 = os.stat(file_dst)
# print(meta1)
# print(meta2)
#
# accessTime = time.ctime ( meta1 [ stat.ST_CTIME ] )
# accessTime2 = time.ctime ( meta2 [ stat.ST_CTIME ] )
#
# print(accessTime)
# print(accessTime2)

# cmd === "Netsh wlan show profile"
# Netsh wlan show profile name = "Miles" key = clear











