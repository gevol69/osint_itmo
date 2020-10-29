import pandas as pd
import csv

def write_csv(dict_data):
    keys = ['date_start', 'time_start', '-', 'date_end', 'time_end']
    with open('user_3.csv', 'a') as csv_file:
        writer = csv.DictWriter(csv_file, keys, delimiter=',')
        writer.writerows([dict_data])


df = pd.read_csv('user_3.log', sep=' ', engine='python')
df.columns = ['date', 'time', 'is_online']
count_true = 0
list_date_and_time_true = []
for index in range(len(df.index)):
    if (df.loc[index, 'is_online'] == True) and count_true < 1:
        count_true += 1
        list_date_and_time_true.append([df.loc[index, "date"], df.loc[index, "time"]])
    if count_true >= 1 and (df.loc[index, 'is_online'] == False):
        count_true = 0
        list_date_and_time_true.append([df.loc[index - 1, "date"], df.loc[index - 1, "time"]])

for index in range(len(list_date_and_time_true) - 1):
    dict_data = {
    'date_start' : list_date_and_time_true[index][0],
    'time_start' : list_date_and_time_true[index][1],
    '-' : '-',
    'date_end' : list_date_and_time_true[index + 1][0],
    'time_end' : list_date_and_time_true[index + 1][1]
    }
    write_csv(dict_data)

