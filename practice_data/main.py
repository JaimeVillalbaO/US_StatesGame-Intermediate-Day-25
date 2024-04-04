# with open('weather_data.csv') as data_file:
#     data_list = data_file.readlines()
#     print(data_list)


import csv


# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         # print(row)
#         if row[1] != 'temp': #para no incluir el primer valor temp
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas as pd 
import numpy

# data = pd.read_csv('weather_data.csv')
# print(type(data)) #frame
# print(type(data['temp'])) #serie

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)

# print(numpy.mean(temp_list))
# print(data['temp'].mean()) #debo colorar en formato de serie, promedip
# print(data['temp'].max())

# # get data in column
# print(data['condition'])
# print(data.condition) # es lo mismo que lo anterior

# # get data in row
# print(data[data['day'] == 'Monday'])
# print(data[data.day == 'Monday'])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# print(monday.condition)
# temp_mond = monday.temp[0]
# temp_fareng = (temp_mond*9/5)+32
# print(temp_fareng)


# create a dataframe from scratch 
# data = {'Nombre': ['Juan', 'Ana', 'Carlos', 'Elena'],
#         'Edad': [25, 30, 22, 28],
#         'Puntuacion': [85, 90, 88, 78]}

# data_frame = pd.DataFrame(data)
# print(data_frame)
# data_frame.to_csv('new_data.csv')


data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231215.csv')

list_color = data['Primary Fur Color'].to_list()
gray_color_counts = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_color_counts = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_color_counts = len(data[data['Primary Fur Color'] == 'Black'])

print(gray_color_counts)
print(cinnamon_color_counts)
print(black_color_counts)

data_dict = {
    'Fur color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_color_counts, cinnamon_color_counts, black_color_counts],
}

df = pd.DataFrame(data_dict)
print(df)
df.to_csv('Squirrel_count.csv')