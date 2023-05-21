import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_data = {
    "Fur Color": ['Gray', 'Black', 'Cinnamon'],
    "Count": [len(data[data['Primary Fur Color'] == 'Gray']), len(data[data['Primary Fur Color'] == 'Black']),
              len(data[data['Primary Fur Color'] == 'Cinnamon'])]
}
data = pandas.DataFrame(squirrel_data)
data.to_csv('squirrel_count.csv')

