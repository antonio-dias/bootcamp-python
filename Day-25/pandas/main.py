# with open("./weather_data.csv") as csv_data:
#     data = csv_data.readlines()
#     print(data)

# import csv
#
# with open("./weather_data.csv") as csv_data:
#     data = csv.reader(csv_data)
#     temperatures = []
#     for index, row in enumerate(data):
#         if index > 0:
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# # average_temp = sum(temp_list) / len(temp_list)
# # print(average_temp)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
fahrenheit = (monday.temp * (9/5)) + 32
print(fahrenheit)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")