import pandas as pd

# read data
data = pd.read_csv('tickets.csv')

# create northbound and southbound dict
northbound = {}
southbound = {}
# define station_count
station_count = data.shape[0]
# define station_list
station_list = []

for i in range(station_count):
    station_list.append(data.iloc[i, 0])
    for j in range(i, station_count):
        if i != j:
            # append to dict
            northbound[(data.iloc[j, 0], data.iloc[i, 0])] = [
                data.iloc[j, i+1], data.iloc[i, j+1]]
            southbound[(data.iloc[i, 0], data.iloc[j, 0])] = [
                data.iloc[j, i+1], data.iloc[i, j+1]]

# (a)
print(northbound['Hsinchu', 'Nangang'])
print(southbound['Nangang', 'Yunlin'])


# (b)
def search():
    '''search the ticket fee between two stations'''
    # input station
    input_station = input('Enter your start and end stations:')
    # ignore space
    station = input_station.replace(' ', '')
    station = station.split(',')

    # station not found
    if (station[0] not in station_list) or (station[1] not in station_list):
        print(
            f'The destination from {station[0]} to {station[1]} is not found')
    # northbound
    elif station_list.index(station[0]) > station_list.index(station[1]):
        print(f'Northbound from {station[0]} to {station[1]}')
        print(
            f'The ticket fare of Standard Car is: {northbound[tuple(station)][0]}')
        print(
            f'The ticket fare of Business Car is: {northbound[tuple(station)][1]}')
    # southbound
    else:
        print(f'Southbound from {station[0]} to {station[1]}')
        print(
            f'The ticket fare of Standard Car is: {southbound[tuple(station)][0]}')
        print(
            f'The ticket fare of Business Car is: {southbound[tuple(station)][1]}')
    return 0


search()
