import pandas as pd


def tickets_init():
    # read data
    data = pd.read_csv('tickets.csv')

    # create northbound and southbound dict
    global northbound
    global southbound
    northbound = {}
    southbound = {}
    # define station_count
    station_count = data.shape[0]
    # define station_list
    global station_list
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


def search(start: str, end: str):
    '''search the ticket fee between two stations'''
    # init result list
    result_text = []
    # concate input
    input_station = start + ',' + end
    # ignore space and enter
    station = input_station.replace(
        ' ', '').replace('\n', '').replace('\r', '')
    station = station.split(',')

    # station not found
    if (station[0] not in station_list) or (station[1] not in station_list):
        result_text.append(
            f'The destination from {station[0]} to {station[1]} is not found')
    # northbound
    elif station_list.index(station[0]) > station_list.index(station[1]):
        result_text.append(f'Northbound from {station[0]} to {station[1]}')
        result_text.append(
            f'The ticket fare of Standard Car is : {northbound[tuple(station)][0]}')
        result_text.append(
            f'The ticket fare of Business Car is : {northbound[tuple(station)][1]}')
    # southbound
    else:
        result_text.append(f'Southbound from {station[0]} to {station[1]}')
        result_text.append(
            f'The ticket fare of Standard Car is: {southbound[tuple(station)][0]}')
        result_text.append(
            f'The ticket fare of Business Car is: {southbound[tuple(station)][1]}')
    return result_text
