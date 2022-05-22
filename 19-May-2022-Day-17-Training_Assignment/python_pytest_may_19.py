# numbers = []
# def while_loop(i, x, y):
#     while i < x:
#         print(f"At the top i is {i}")
#         numbers.append(i)
#         i = i+y
#         print("Numbers now: ", numbers)
#         print(f"At the bottom is {i}")
#     print("The numbers: ")
#     for num in numbers:
#         print(num)
# while_loop(0, 6, 1)
#
#
# from random import seed
# from random import randint
#
# seed(1)
#
# for _ in range(10):
#     value = randint(0, 10)
#     print(value)

# def appendMiddle(s1, s2):
#     middleIndex = int(len(s1)/2)
#     print("Original Strings are", s1, s2)
#     middleThree = s1[:middleIndex:] + s2 + s1[middleIndex:]
#     print("After appending new string in middle", middleThree)
#
# appendMiddle("Ault", "Kelly")

# var = ['ab', 'cde', 'de', 'running', 'good']
#
# print(var)


# import json
# from json import JSONEncoder
# class Vehicle:
#
#     def __init__(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price
#
# class VehicleEncoder(JSONEncoder):
#     def default(self, o):
#         return o.__dict__
#
# vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
#
# print("Encode Vehicle object into JSON")
#
# vehicleJson = json.dumps(vehicle, indent = 4, cls = VehicleEncoder)
#
# print(vehicleJson)


################### Q1 ###################################

# n = int(input())
#
# flag = 0
#
# for i in range(2, n//2 + 1):
#     if n%i == 0:
#         flag = 1
#
# if flag != 0:
#     print("Not a prime")
# else:
#     print("Prime")


######################## Q2 ################################


