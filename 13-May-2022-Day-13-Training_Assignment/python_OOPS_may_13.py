
#########Class and Objects

# class My_Class:
#
#     def fun():
#         print("welcome to python")
#
#     def two():
#         print("welcome to OOPS")
# My_Class.fun()
# My_Class.two()

# class My_Class:
#
#     def fun():
#         print("welcome to python")
#
#     def two():
#         print("welcome to OOPS")
# my = My_Class
# my.fun()
# my.two()
#
#
# class My_Server(object):
#
#     def __init__(self, ip, pwd):
#         self.ip = ip
#         self.pwd = pwd
#
#     def server_login(self):
#         print("welcome to python", self.ip)
#
#     def hostname(self):
#         print("welcome to OOPS", self.ip, self.pwd)
#
# my = My_Server("2.2.2.2","897")

#Every class inherits object
# My_Server()is called constructor
# my is now becomes instance object reference
# When we create constructor, we will have one hidden object created inside the constructor
# __init__ by nature is called as attribute or magic methods or dunder methods
# __init__ will be created automatically when class constructor got created
# __init__as functionality we call as instance + initializer =  ---instantiator
# __new__
# my.server_login()
# my.hostname()


# class My_Server(object):
#     """__author__ Geashna D
#     __data__ May 13, 2022
#     Class name: My_Server"""
#
#     def __init__(self, ip, pwd):
#         self.ip = ip
#         self.pwd = pwd
#
#     def server_login(self,country):
#         print("welcome to python", self.ip,country)
#
#     def hostname(self):
#         print("welcome to OOPS", self.ip, self.pwd)
#
#     @staticmethod #decorator
#     def routing(url):
#         print(url)
#
# my = My_Server("2.2.2.2","897")
# my.server_login("India")
# my.hostname()
# print(my.__doc__)
# my.routing("https://futurense.com")

# class My_Server(object):
#
#     def __init__(self, ip, pwd):
#         self.ip = ip
#         self.pwd = pwd
#
#     def __server_login(self,country): #__private access specifier, data encapsulation, hiding
#         print("welcome to python", self.ip,country)
#
#     def hostname(self):
#         print("welcome to OOPS", self.ip, self.pwd)
#
#
# my = My_Server("2.2.2.2","897")
# #my.server_login("India") --error
# my.hostname()

###################################### Function Scope ############################################

# var = 100
# def fun():
#     var =10
#     print(var)
# print(var)
# fun()
# print(var)


# var = 100
# def fun():
#     global var
#     var =10
#     print(var)
# print(var)
# fun()
# print(var)

#Scoping

# var = 1000 #Global
# def fun():
#     var =100 #Enclosed
#
#     def new():
#         var =10 #Local
#         print(var)
#     new()
#
# fun()

# counter = 0
# def fun():
#     global counter
#     counter += 1
#     print("hello",counter)
#     fun()
#
# fun()


####### terminate with return
# counter = 0
# def fun():
#     global counter
#     counter += 1
#     if counter == 100:
#         return
#     print("hello",counter)
#     fun()
#
# fun()

####### terminate without return
# counter = 0
# def fun():
#     global counter
#     counter += 1
#     print("hello",counter)
#     if counter < 100:
#         fun()
#
# fun()


# counter = 0
# def fun():
#     global counter
#     counter += 1
#     print("hello",counter)
#     while counter < 100:
#         fun()
# fun()


#difference between return and yield
#yield is for generator


# def fun():
#
#     var = 10
#     return var
#
#     var+=10
#     return var
#
#     var+=20
#     return var
#
# f = fun()
# print(f)
# print(f)
# print(f)

# def fun():
#
#     var = 10
#     yield var
#
#     var+=10
#     yield var
#
#     var+=20
#     yield var
#
# f = fun()
# print(next(f))
# print(next(f))
# print(next(f))


# class My_Server(object):
#
#     def __init__(self, ip, pwd):
#         self.ip = ip
#         self.pwd = pwd
#
#     def server_login(self,country):
#         print("welcome to python", self.ip,country)
#     #def server_login(self): ---error because no overloading in python
#         #print("welcome to python", self.ip,country)
#
# my = My_Server("2.2.2.2","897")
# my.server_login("India")


#################################   Inheritance #######################################


# class My_Server(object):
#
#     def __init__(self, ip, pwd):
#         self.ip = ip
#         self.pwd = pwd
#
#     def server_login(self):
#         print("welcome to python", self.ip)
#
# class Second_Class(My_Server): #inheritance
#
#     def Login(self):
#         print("welcome to python --child",self.ip, self.pwd)
#
# my = Second_Class("2.2.3.4","675")
# my.server_login()
# my.Login()

# class My_Server(object):
#
#     def server_login(self):
#         print("welcome to python")
#
# class Second_Class(My_Server): #inheritance
#
#     def __init__(self, ip, pwd):
#         self.ip = ip
#         self.pwd = pwd
#
#     def Login(self):
#         print("welcome to python --child",self.ip, self.pwd)
#
# my = Second_Class("2.2.3.4","675")
# my.server_login()
# my.Login()

# class My_Server(object):
#
#     def __init__(self, ip, pwd):
#         self.ip = ip
#         self.pwd = pwd
#
#     def server_login(self):
#         print("welcome to python", self.ip)
#
# class Second_Class(My_Server): #inheritance
#
#     def __init__(self, ip, pwd):
#         self.ip = ip
#         self.pwd = pwd
#
#     def Login(self):
#         print("welcome to python --child",self.ip, self.pwd)
#
# my = Second_Class("2.2.3.4","675")
# my.server_login()
# my.Login()

###### Inducing data to parent through child
# class My_Server(object):
#     def __init__(self, ip, pwd, country):
#         self.ip = ip
#         self.pwd = pwd
#         self.country = country
#     def server_login(self):
#         print("welcome to python", self.ip, self.country)
#
# class Second_Class(My_Server): #inheritance
#
#     def __init__(self, ip, pwd):
#         self.ip = ip
#         self.pwd = pwd
#         #My_Server.__init__(self, self.ip, self.pwd, "india")
#         super().__init__(self.ip, self.pwd, "india")
#     def Login(self):
#         print("welcome to python --child",self.ip, self.pwd)
#
# my = Second_Class("2.2.3.4","675")
# my.server_login()
# my.Login()



##########################################        Task        ######################################################
#
# class Create:
#
#     def __init__(self, table_name, db):
#         self.table_name = table_name
#         self.db = db
#
#     def My_DB_Select(self):
#
#         try:
#             connection = ""
#             connection = sqlite3.connect("python.db")
#             query = """CREATE TABLE Student2 ("name" text, "age" int)"""
#             execution = connection.execute(query)
#         except Exception as ex:
#             print(ex)
#         finally:
#             if connection != "":
#                 connection.commit()
#                 connection.close()
#
#
# obj = Create(db="new.db", table_name="sachin")
# obj.My_DB_Select()








