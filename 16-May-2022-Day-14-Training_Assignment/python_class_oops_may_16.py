# class one:
#     def __init__(self, name):
#         self.name = name
#     def onefun(self):
#         print(self.name)
#
# class two:
#     def __init__(self,age):
#         self.age = age
#         self.test = one("dhoni") #Composition
#         self.test.onefun()
#
#     def twofun(self):
#         print(self.age)
#
# t = two(23)
# t.twofun()

### ----------------------------------------------------------------------------------

# class one:
#     def __init__(self, name):
#         self.name = name
#     def onefun(self):
#         print(self.name)
#
# class two:
#     def __init__(self, age, fobj):
#         self.age = age
#         self.name = fobj  # Aggregation
#         fobj.onefun()
#     def twofun(self):
#         print(self.age)
#
# fobj = one("kohli")
# t = two(23, fobj)
# t.twofun()



######---------------------------------------------------------------------------------------------------------

# class A:
#     def fun(self):
#         print("A")
#
# class B(A):
#     def fun(self):
#         print("B")
#
# class C(A):
#     def fun(self):
#         print("C")
#
# class D(B, C): #check for D(C,B)
#     pass
#     # def fun(self):
#     #     print("D")

# d = D()
# d.fun()

##MRO ----> Method Resolution order
##Near By Search (2.7 version has Deep Search)


########---------------------------------------------------------------------------------------------------------------

# import pandas as pd
#
# df = pd.DataFrame({'name': ['alice','bob', 'charlie'], 'date_of_birth' : ['10/25/2003', '05/25/2000','05/01/1999']})
#
# print(df)
#
# df['date_of_birth'] = pd.to_datetime(df['date_of_birth'])
#
# print(df)


####-------------------------------------------------------------------------------------------------------------------

# import pandas as pd
#
# df = pd.DataFrame({'name': ['alice','bob', 'charlie'], 'date_of_birth' : ['10/25/2003', '05/25/2000','05/01/1999']})
#
# print(df)
#
# df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], format = '%m/%d/%Y')
# #df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], format = '%d/%m/%Y')
# print(df)


#### -------------------------------------------------------------------------------------------------------------------

# import pandas as pd
# from datetime import datetime
#
# df = pd.DataFrame({"name":["alice","bob","charlie","david"],"age":[12,43,22,16]})
#
# df["timestamp_col"] = pd.Timestamp(datetime.now())
#
# df["formatted_col"] = df["timestamp_col"].map(lambda ts: ts.strftime("%d-%m-%Y"))
#
# print(df)


##### ------------------------------------------------------------------------------------------------------------------

# import pandas as pd
#
# from datetime import date
#
# df = pd.DataFrame({'name':['alice', 'bob', 'chalie'],'date_of_birth': ['10/25/2000','10/29/1999','01/01/2001']})
#
#
# #conver to type datetime
#
# df['date_of_birth'] = pd.to_datetime(df['date_of_birth'])
# df[df['date_of_birth'] < pd.Timestamp(date(2000,1,1))]
#
# print(df)


##### ------------------------------------------------------------------------------------------------------------------

# import pandas as pd
#
# from datetime import date
#
# df = pd.DataFrame({'name':['alice', 'bob', 'chalie'],'date_of_birth': ['10/25/2000','10/29/1999','01/01/2001']})
#
#
# #conver to type datetime
# df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], format = '%m/%d/%Y')
#
# output = df[df['date_of_birth'] < pd.Timestamp(date(2000,1,1))]
#
# print(output)

##### ------------------------------------------------------------------------------------------------------------------

# import pandas as pd
#
# from datetime import date
#
# df = pd.DataFrame({'name':['alice', 'bob', 'chalie'],'date_of_birth': ['10/25/2004','10/29/1999','01/01/2005']})
# date_from = pd.Timestamp(date(2003, 1, 1))
# date_to = pd.Timestamp(date(2006, 1, 1))
# df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], format = '%m/%d/%Y')
# df = df[(df['date_of_birth'] > date_from) & (df['date_of_birth'] < date_to)]
#
# print(df)