from datetime import datetime

def filter_by_state(my_list, state='EXECUTED'):
    filtered_list = []
    for i in my_list:
        if i['state'] == state:
            filtered_list.append(i)
    return filtered_list


# print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))


def sort_by_date(my_list, ascending=True):
    # Функция для преобразования строки даты в объект datetime
    def parse_date(date):
        return datetime.fromisoformat(item['date'])

    sorted_list = []
    for item in my_list:
        sorted_list = sorted(my_list, key=parse_date, reverse=ascending)

    return sorted_list


# print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
