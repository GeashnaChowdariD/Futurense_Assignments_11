import pandas
'''
my_input = [2, 3, 4, 5]

list_manipulation = my_input*2

print(list_manipulation)

my_dimension = pandas.DataFrame(my_input)

print(my_dimension)


print(type(my_dimension))



my_input = [[1,2,3,4],[8, 7, 9], [4, 5, 6], [5,1,2,3,4]]

two_dim_list_manipulation = my_input*2

print(two_dim_list_manipulation)

dimension_of_input = pandas.DataFrame(my_input)

print(dimension_of_input)

print(type(dimension_of_input))

inp = [1, 'h', 3, ['q', 'w', 'e', 'r']]

dimension_of_hetero_list = pandas.DataFrame(inp)

print(dimension_of_hetero_list)

print(type(dimension_of_hetero_list))


my_input = (2, 3, 4, 5)

list_manipulation = my_input*2

print(list_manipulation)

my_dimension = pandas.DataFrame(my_input)

print(my_dimension)


print(type(my_dimension))



my_input = [2, 3, 4, 5]

list_manipulation = my_input*2

print(list_manipulation)

my_dimension = pandas.DataFrame(my_input)

print(my_dimension)

sum_of_list = my_dimension.sum()
print(sum_of_list)


inp_2 = [[2,3,4,5],[4,5,6,7,8]]
my_dimension = pandas.DataFrame(inp_2)
print(my_dimension)
sum_of_list = my_dimension.sum()
print(sum_of_list)

inp_2 = [[2,3,4,5],[4,5,6,7,8]]
my_dimension = pandas.DataFrame(inp_2, index = ["a","b"], columns= ['A', 'B', 'C', 'D', 'E'
                                                                                        ''])
print(my_dimension)
sum_of_list = my_dimension.sum(axis = 1)
print(sum_of_list)


inp_3 = {"names" : ["dhoni", "kohli"], "team":["csk", "rcb"]}

my_dimension = pandas.DataFrame(inp_3, index = ["a", "b"], columns=['A', 'B', 'C', 'D'])
print(my_dimension)


inp_3 = {"names" : ["dhoni", "kohli"], "team":["csk", "rcb"]}

my_dimension = pandas.DataFrame(inp_3,columns=['A', 'B', 'C', 'D'])
print(my_dimension)


inp_3 = {"names" : ["dhoni", "kohli"], "team":["csk", "rcb"]}

my_dimension = pandas.DataFrame(inp_3, index = ["a", "b"])
print(my_dimension)


inp_3 = {"names" : ["dhoni", "kohli"], "team":["csk", "rcb"]}

my_dimension = pandas.DataFrame(inp_3, index = ["a", "b"])
print(my_dimension)

print(my_dimension.loc["a"])
print(my_dimension.iloc[0,1])

my_dimension.to_csv("testing.csv")



##group by

data = {
  'co2': [95, 90, 99, 104, 105, 94, 99, 104],
  'model': ['Citigo', 'Fabia', 'Fiesta', 'Rapid', 'Focus', 'Mondeo', 'Octavia', 'B-Max'],
  'car': ['Skoda', 'Skoda', 'Ford', 'Skoda', 'Ford', 'Ford', 'Skoda', 'Ford']
}

df = pandas.DataFrame(data)

print(df.groupby(["car"]).sum())

print(df.groupby(["car"]).mean())


data = {"score":[90,20,25,36], "player":["dhoni","dhoni","kohli","rohit"]}

df_data= pandas.DataFrame(data)
mean_data = df_data.groupby(["player"]).mean()
print(mean_data)


data = {"runs": [1, 2, 3, 1],"score":[90,20,95,36], "player":["dhoni","dhoni","kohli","rohit"]}

df_data= pandas.DataFrame(data)
mean_data = df_data.groupby(["player"]).mean()
print(mean_data)


data = {"runs": [1, 2, 3, 1],"score":[90,20,95,36], "player":["dhoni","dhoni","kohli","rohit"]}

df_data= pandas.DataFrame(data)
mean_data = df_data.groupby(["player"])["runs"].mean()
print(mean_data)

data = {"runs": [1, 2, 3, 1],"score":[90,20,95,36], "player":["dhoni","dhoni","kohli","rohit"]}

df_data= pandas.DataFrame(data)
mean_data = df_data.groupby(["player"], sort = False)["runs"].mean()
print(mean_data)

data_csv = pandas.read_csv('devi.csv')

print(data_csv.groupby(['subject']).min())

data_csv = pandas.read_csv('devi.csv')

print(data_csv.groupby(['subject']).max())
'''

data_csv = pandas.read_csv('devi.csv')

print(data_csv.groupby(['subject','names'],sort=False).max())

data_csv = pandas.read_csv('devi.csv')

print(data_csv.groupby(['subject'],sort=False).max())















