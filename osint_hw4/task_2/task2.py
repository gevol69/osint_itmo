import csv 
from datetime import datetime
import time

def write_csv(dict_data):
    keys = ['date', 'time', 'is_online']
    with open('user_3.csv', 'a') as csv_file:
        writer = csv.DictWriter(csv_file, keys, delimiter=',')
        writer.writerows([dict_data])

def dict_create(timestamp, is_online):
    timestamp_to_date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    date = timestamp_to_date.split(' ')[0]
    time = timestamp_to_date.split(' ')[1]
    dict_data = {
    'date' : date, 
    'time' : time, 
    'is_online' : is_online
    }
    return dict_data

list_sort_timestamp =  []

with open('user_3.txt', 'r') as file_handler:
    for line in file_handler:
        from_timestamp = int(line.split(' ')[0].strip())
        to_timestamp = int(line.split(' ')[1].strip())
        list_sort_timestamp.append([from_timestamp, to_timestamp])


list_sort_timestamp = sorted(list_sort_timestamp)

for index in range(len(list_sort_timestamp)):
    for timestamp in range(list_sort_timestamp[index][0], list_sort_timestamp[index][1], 5):
        is_online = True
        dict_data = dict_create(timestamp, is_online)
        write_csv(dict_data)
    try:
        for timestamp in range(list_sort_timestamp[index][1], list_sort_timestamp[index + 1][0], 5):
            is_online = False
            dict_data = dict_create(timestamp, is_online)
            write_csv(dict_data)
    except IndexError:
        is_online = True
        timestamp = list_sort_timestamp[-1][1]
        dict_data = dict_create(timestamp, is_online)
        write_csv(dict_data)



