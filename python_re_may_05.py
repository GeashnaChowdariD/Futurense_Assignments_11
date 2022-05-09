

import re
var = "dhoni is better than rohit"
data = re.match("dhoni",var)
print(data)
print(data.group())
print(data.span())
print(data.start())
print(data.end())

var = "dhoni is better than rohit"
data = re.search("is",var)
print(data)
print(data.group())

var2 = "Dhoni is better than rohit"
data = re.search("Is",var2,re.I)
print(data)
print(data.group())


var4 = """dhoni is better than kohli
dhoni plays well
dhoni is senior than kohli"""

data = re.match("dhoni",var4,re.I)
print(data)
print(data.group())

var4 = '''dhoni is better than kohli
dhoni plays well
sachin is senior than kohli'''

data = re.match("dhoni",var4,re.M)
print(data)
print(data.group())

var = "<html><body><head><script>"
data = re.search("<.*>",var)
print(data.group())

var = "<html><body><head><script>"
data = re.search("<.*?>",var)
print(data.group())

var = "dhoni is better than rohit"
data = re.search("(.*) is (.*)", var)
print(data.group())
print(data.group(1))
print(data.group(2))

var = "dhoni is better than rohit"
data = re.search("(.*) is (.*?) (.*)", var)
print(data.group())
print(data.group(1))
print(data.group(2))
print(data.group(3))

var = "DHONI scored 183 against SRIlanka @ 2009 with 7.5 Avg per OVER!!! "
data = re.findall("\d{1,3}",var)
print(data)

var = "DHONI scored 183 against SRIlanka @ 2009 with 7.5 Avg per OVER!!! "
data = re.findall("\d{3}",var)
print(data)

var = "DHONI scored 183 against SRIlanka @ 2009 with 7.5 Avg per OVER!!! "
data = re.findall("\D{1,3}",var)
print(data)

var = "DHONI scored 183 against SRIlanka @ 2009 with 7.5 Avg per OVER!!! "
data = re.findall("\D{3}",var)
print(data)

var = "DHONI scored 183 against SRIlanka @ 2009 with 7.5 Avg per OVER!!! "
data = re.findall("\w",var)
print(data)

var = "DHONI scored 183 against SRIlanka @ 2009 with 7.5 Avg per OVER!!! "
data = re.findall("\w*",var)
print(data)

var = "DHONI scored 183 against SRIlanka @ 2009 with 7.5 Avg per OVER!!! "
data = re.findall("\w+",var)
print(data)

var = "DHONI scored 183 against SRIlanka @ 2009 with 7.5 Avg per OVER!!! "
data = re.findall("\W",var)
print(data)

var = "DHONI scored 183 against SRIlanka @ 2009 with 7.5 Avg per OVER!!! "
data = re.findall("\W*",var)
print(data)

var = "DHONI scored 183 against SRIlanka @ 2009 with 7.5 Avg per OVER!!! "
data = re.findall("\W+",var)
print(data)

var = "DHONI scored 183 against SRIlanka @ 2009 with 7.5 Avg per OVER!!! "
data = re.findall("\s",var)
print(data)

var = "DHONI scored 183 against SRIlanka @ 2009 with 7.5 Avg per OVER!!! "
data = re.findall("\s*",var)
print(data)

var = "DHONI scored 183 against SRIlanka @ 2009 with 7.5 Avg per OVER!!! "
data = re.findall("\s+",var)
print(data)

var = "DHONI scored 183 against SRIlanka @ 2009 with 7.5 Avg per OVER!!! "
data = re.findall("\s*",var)
print(data)

var = "DHONI scored 183 against SRIlanka @ 2009 with 7.5 Avg per OVER!!! "
data = re.findall("\S",var)
print(data)

var = "DHONI scored 183 against SRIlanka @ 2009 with 7.5 Avg per OVER!!! "
data = re.findall("\S*",var)
print(data)

var = "DHONI scored 183 against SRIlanka @ 2009 with 7.5 Avg per OVER!!! "
data = re.findall("\S+",var)
print(data)


import time
import threading

def fun1():
    print("one")
    print(time.ctime())
    time.sleep(2)

def fun2():
    print("two")
    print(time.ctime())

fun1()
fun2()

def fun1(name):
    print(name)
    print(time.ctime())
    time.sleep(2)

def fun2(name):
    print(name)
    print(time.ctime())


t1 = threading.Thread(target = fun1, args = ("dhoni",))
t2 = threading.Thread(target = fun2, args = ("kohli",))

t1.start()
t2.start()

t1.join()
t2.join()

def fun1(name,delay):
    counter = 0
    while counter < 5:
        print(name)
        print(time.ctime())
        time.sleep(delay)
        counter += 1

t1 = threading.Thread(target = fun1, args = ("dhoni",2))
t2 = threading.Thread(target = fun1, args = ("kohli",4))

t1.start()
t2.start()

t1.join()
t2.join()
