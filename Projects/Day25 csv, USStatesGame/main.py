# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(data.temp)
# print(type(data)) -> DataFrame
# print(type(data["temp"])) -> Series

# data_dict = data.to_dict()
# # print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

#Average temp
# print(data["temp"].mean())
# print(data["temp"].max())

#Get a Data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

#Create a dataframe from scratch.
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("new_data.csv")



################# Squirrels ##################
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

num_grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
num_red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
num_black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [num_grey_squirrels, num_red_squirrels, num_black_squirrels]
}

df = pandas.DataFrame(squirrel_dict)
df.to_csv("squirrel_count.csv")