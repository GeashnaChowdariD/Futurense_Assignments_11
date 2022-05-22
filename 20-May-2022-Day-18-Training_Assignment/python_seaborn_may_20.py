##########################################################################################################
# # class MyError(Exception):
# #     my_meaning = "user defined exception"
# #
# # try:
# #     var=10
# #     if var>5:
# #         raise MyError
# # except MyError as ex:
# #     print(ex.my_meaning)
# # pdb.set_trace()
# #
# # print("hello")
#############################################################################################################
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# #CSV read
# try:
#
#     df = pd.read_csv(r"E:\Futurense_training_online\deliveries.csv",sep=",")
#     # df.head(20)
#     # print(df.head())
#     df.columns = ["batting_team", "batsman", "total_runs"]
#     df_by_batsman = df.groupby("batting_team")["total_runs"].sum().reset_index()
#     print(df_by_batsman)
#     sns.set_style('darkgrid')
#     sns.barplot(y=df_by_batsman.total_runs, x=df_by_batsman.batting_team, data=df_by_batsman, palette='plasma')
#     plt.show()
#
# except Exception as ex:
#     print(ex)



#######################################################################################################################
import math

def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

def testsquare():
    num = 7
    assert 7*7 == 40

def testquality():
    assert 10 ==11

test_sqrt()