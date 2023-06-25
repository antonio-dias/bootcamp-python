import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(data["Primary Fur Color"])

dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [
        len(data[data["Primary Fur Color"] == "Gray"]),
        len(data[data["Primary Fur Color"] == "Cinnamon"]),
        len(data[data["Primary Fur Color"] == "Black"]),
    ]
}

final_csv = pandas.DataFrame(dict)

final_csv.to_csv("new_base.csv")