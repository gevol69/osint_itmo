from datetime import datetime
from collections import Counter

dict_timestamp_users = {
    0 : [],
    1 : [],
    2 : [],
    3 : [],
    4 : [],
    5 : [],
    6 : [],
    7 : [],
    8 : [],
    9 : [],
    10 : [],
    11 : [],
    12 : [],
    13 : [],
    14 : [],
    15 : [],
    16 : [],
    17 : [],
    18 : [],
    19 : []
}

def get_dates_online_user(id_user):
    list_dates = []
    for list_timestamp in dict_timestamp_users[id_user]:
        from_timestamp = datetime.utcfromtimestamp(list_timestamp[0]).strftime('%Y-%m-%d %H:%M:%S')
        to_timestamp = datetime.utcfromtimestamp(list_timestamp[1]).strftime('%Y-%m-%d %H:%M:%S')
        list_dates.append('{} - {}'.format(from_timestamp, to_timestamp))
    return list_dates

with open('user_3_task4.txt', 'r') as file_handler:
    for line in file_handler:
        id_user = int(line.split(' ')[0].strip())
        from_timestamp = int(line.split(' ')[1].strip())
        to_timestamp = int(line.split(' ')[2].strip())
        dict_timestamp_users[id_user].append([from_timestamp, to_timestamp])

for key in dict_timestamp_users.keys():
    dict_timestamp_users[key] = sorted(dict_timestamp_users[key])

if __name__ == "__main__":
    id_users = input().split(' ')
    id_users = list(map(int,  id_users))
    list_dates_online = []
    for id_user in id_users:
        print("Пользователь {} был в онлайне в следующие промежутки времени:".format(id_user))
        for date in get_dates_online_user(id_user):
            print(date)
