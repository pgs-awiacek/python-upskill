import csv
import json
from pathlib import Path
from participant import *
from prize import *


def load_csv(path):
    with open(path) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        data = list(reader)
    return data


def load_json(path):
    with open(path) as json_file:
        reader = json.load(json_file)
    return reader


# class Result:
#     def __init__(self, name, amount, first_name, last_name):
#         self.name = name
#         self.amount = amount
#         self.first_name = first_name
#         self.last_name = last_name


def print_list_of_winners(winners_list, prizes_list):
    for data in range(len(winners_list)):
        print(winners_list[data].first_name, winners_list[data].last_name, '->', prizes_list[data])
    return data


if __name__ == '__main__':
    DATA_DIR = Path('data/')
    TEMPLATES_DIR = Path(DATA_DIR / 'lottery_templates/')
    participants_csv_raw_data = load_csv(DATA_DIR / 'participants1.csv')
    participants_json_raw_data = load_json(DATA_DIR / 'participants1.json')
    item_giveaway = load_json(TEMPLATES_DIR / 'item_giveaway.json')
    separate_prizes = load_json(TEMPLATES_DIR / 'separate_prizes.json')

    participants_csv_list = create_participant_list(data=participants_csv_raw_data)
    participants_json_list = create_participant_list(data=participants_json_raw_data)

    item_prizes_amount = get_prizes_amount(item_giveaway)
    medal_prizes_amount = get_prizes_amount(separate_prizes)

    medal_prizes_list = get_prizes_list(separate_prizes)
    medal_winners_list = pick_winners(participants_json_list, medal_prizes_amount)
    print_list_of_winners(medal_winners_list, medal_prizes_list)

    print('xxxxxxxxxxxx')

    item_prizes_list = get_prizes_list(item_giveaway)
    item_winners_list = pick_winners(participants_csv_list, item_prizes_amount)
    print_list_of_winners(item_winners_list, item_prizes_list)
