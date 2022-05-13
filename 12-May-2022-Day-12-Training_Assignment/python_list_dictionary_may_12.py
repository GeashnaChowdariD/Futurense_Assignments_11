# var = []
# print(type(var))
#
# var = list()
# print(type(var))
#
#
# var = ["dhoni","kohli"]
# var[1] = "Rahul"
# print(var)

# var = ["dhoni"]
# var1 = ["kohli"]
# print(var + var1)

# var =  ["dhoni","kohli"]
# #var[5] = "Rohit" --error
# print(var)

# var = ["dhoni","kohli"]
# var.insert(5,"rohit")
# print(var)

# var = ["dhoni","kohli"]
# var.append("rohit")
# print(var)
#
# var = ["dhoni","kohli"]
# #var.append("rahul","rohit") --error
# print(var)
#
# var = ["dhoni","kohli"]
# var.append(["rahul","rohit"])
# print(var)
#
# var = ["dhoni","kohli"]
# var.append(("rahul","rohit"))
# print(var)

###Task ---- Collections Module

# from collections import Counter
# dict_a = {"A":2,"B":5, "C":6, "D":7}
# list_a = ['A','C','B', 'D', 'F', 'E', 'C','D', 'C']
# print(Counter(dict_a))
# print(Counter(list_a))

# var = ["dhoni", "kohli",7,6]
# var.extend(("rahul","rohit"))
# print(var)
#
# var = ["dhoni", "kohli",7,6]
# #var.extend("rahul","rohit") --error
# print(var)
#
# var = ["dhoni", "kohli",7,6]
# var.extend(["rahul","rohit"])
# print(var)
#
# var = ["dhoni", "kohli", "5","9","19","ashwin"]
# var.sort()
# print(var)
#
# var = ["dhoni", "kohli", "5","9","19","ashwin"]
# var.sort(reverse=True)
# print(var)
#
# var = ["dhoni", "kohli", "5","9","19","ashwin"]
# print(var.sort(reverse=True))
#
# var = ["dhoni", "kohli", "5","9","19","Ashwin", "Arun","ashwin"]
# output = sorted(var,reverse=True,key = len)
# print(output)


# list_a = ["ashwin","cat","basket","aisle", 5, 3, 2, 7, 8, 9, 5.6, ("a","b")]
#
# def mixs(num):
#     try:
#         ele = int(num)
#         return (0, ele, '')
#     except ValueError:
#         return (1, num, '')
#
#
# # initialize list
# test_list = ["ashwin","cat","basket","aisle", 5, 3, 2, 7, 8, 9, 5.6, ("a","b")]
#
# # printing original list
# print("The original list : " + str(test_list))
#
# # Sort Mixed List
# # using sort() + comparator
# for i in range(len(test_list)):
#     if type(test_list[i]) == str or type(test_list[i]) == int or type(test_list[i]) == float:
#         pass
#     else:
#         test_list.remove(test_list[i])
# for i in range(len(test_list)):
#     if type(test_list[i]) == str:
#         test_list[i] = test_list[i][::-1]
#
# test_list.sort(key=mixs)
#
# # printing result
# print("List after mixed sorting : " + str(test_list))

# import sys
#
# var = ()
# print(type(var))
#
# var = ("dhoni")
# print(type(var))
#
# var = ("dhoni",)
# print(type(var))
#
# var = ("dhoni","kohli")
# print(var)
# print(type(var))
# print(sys.getsizeof(var))
#
# var = ["dhoni","kohli"]
# print(var)
# print(type(var))
# print(sys.getsizeof(var))


# var = {}
# print(type(var))
#
# var = {"name":"dhoni", "age":33,"age":[44,22]}
# print(var)
# print(type(var))
#
# ### var = {"name":"dhoni", "age":33,"age":[44,22], ["a","b"]:"kohli"} --- error mutable key
#
# #Hashing or Hash table
# #o(1)
# # key value pair
# # key should be unique and immutable
# # JSON
#
#
# var = {"name":"dhoni", "age":33,"age":[44,22]}
# var["age"][1] = 55
# print(var)
# print(type(var))
#
# #pprint
# #colorma
#var = {"name":"dhoni", "age":33,"age":[44,22]}

# var = [1,"a", 2, "b", 3, "c"]
# var_iter  = iter(var)
# print(var_iter)
# var_zip = dict(zip(var_iter, var_iter))
# print(var_zip)  #{1: 'a', 2: 'b', 3: 'c'}


# var = [4, 5, 6].pop()
# var += 50
# print(var)
#
# var = [4, 5, 6]
# var.pop()
# print(var)


#import sqlite3

# connection = sqlite3.connect("python.db")
# query = """CREATE TABLE Student ("name" text, "age" int)"""
# execution = connection. execute(query)
# connection.commit()
# connection.close()


# def My_DB_Execution(): # function without arguments
#     connection = sqlite3.connect("python.db")
#     query = """CREATE TABLE Student ("name" text, "age" int)"""
#     execution = connection.execute(query)
#     connection.commit()
#     connection.close()
#
# My_DB_Execution()
#
# def My_DB_Execution(table_name, db): # function with arguments
#     connection = sqlite3.connect(db
#     query = f"""CREATE TABLE {table_name} ("name" text, "age" int)"""
#     execution = connection.execute(query)
#     connection.commit()
#     connection.close()
#
# My_DB_Execution("sports","dhoni.db")
#
#
# def My_DB_Execution(table_name, db = "testing.db"): # function with default arguments
#     connection = sqlite3.connect(db
#     query = f"""CREATE TABLE {table_name} ("name" text, "age" int)"""
#     execution = connection.execute(query)
#     connection.commit()
#     connection.close()
#
# My_DB_Execution("sports","dhoni.db")
#
#
# def My_DB_Select(table_name = "sports", db = "testing.db"): # function with default arguments
#     connection = sqlite3.connect(db
#     query = f"""SELECT * FROM {table_name}"""
#     execution = connection.execute(query)
#     connection.commit()
#     connection.close()
#
# My_DB_Select("sports","dhoni.db")


# def My_DB_Execution(table_name="sports", db = "testing.db"): # function with keyword arguments
#     connection = sqlite3.connect(db
#     query = f"""CREATE TABLE {table_name} ("name" text, "age" int)"""
#     execution = connection.execute(query)
#     connection.commit()
#     connection.close()
#
# My_DB_Execution("sports","dhoni.db")

###Task ---- Dictionary Functions


# var = {"name":"dhoni", "age":33,"age":[44,22]}
# print(dir(var))
# var.clear()
# print(var)
# var = {"name":"dhoni", "age":33,"age":[44,22]}
# var1 = var.copy()
# print(var)
# print(var1)
#
# x = ('key1', 'key2', 'key3')
# y = 0
# thisdict = dict.fromkeys(x,y)
# print(thisdict)
#
# x = ('key1', 'key2', 'key3')
# thisdict = dict.fromkeys(x)
# print(thisdict)

# var = 10/0
# print(var)
#
# try:
#     var = "a" + 10
#     print(var)
# except:
#     print("sorry")
#
# try:
#     var = 10/0
#     print(var)
# except TypeError as ex:
#     print(ex)
# except ZeroDivisionError as ex:
#     print(ex)
# except:
#     print("sorry err")

# try:
#     var = 10/0
#     print(var)
# except (TypeError,ZeroDivisionError) as ex:
#     print(ex)
# except:
#     print("sorry err")


# try:
#     var = 10/0
#     print(var)
# except Exception as ex:
# #     print(ex)
#
# try:
#     var = 10/4
#     print(var)
# except Exception as ex:
#     print(ex)
# else:
#     print("else")
# finally:
#     print("welcome")

# try:
#     var=10
#     if var>5:
#         raise IndexError
# except IndexError:
#     print("sorry")


# try:
#     var=10
#     if var>5:
#         raise IndexError
# except IndexError as ex:
#     print(ex)


# try:
#     var=10
#     if var>5:
#         raise IndexError("this is my exception")
# except IndexError as ex:
#     print(ex)

# try:
#     var=10
#     if var>5:
#         #raise MyError --error
# except MYError:
#     print("sorry")

# class MyError(Exception):
#     my_meaning = "user defined exception"
#
# try:
#     var=10
#     if var>5:
#         raise MyError
# except MyError as ex:
#     print(ex.my_meaning)




