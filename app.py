import csv
import json
from pathlib import Path
from participant import create_participant_list, pick_winners
from prize import get_prizes_amount, get_prizes_list


def load_csv(path):
    with open(path) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        data = list(reader)
    return data


def load_json(path):
    with open(path) as json_file:
        reader = json.load(json_file)
    return reader


def create_list_of_winners(winners_list, prizes_list):
    result_list = []
    for data in range(len(winners_list)):
        first_name = winners_list[data].first_name
        last_name = winners_list[data].last_name
        prize_name = prizes_list[data].name
        result_list.append([first_name, last_name, prize_name])
        # result_list.append(last_name)
        # result_list.append(prize_name)
    return result_list


def print_list_of_winners(result_list):
    for data in result_list:
        first_name = data[0]
        last_name = data[1]
        prize_name = data[2]
        print(f'{first_name} {last_name} -> {prize_name}')


# def print_list_of_winnersss(winners_list, prizes_list):
#     for data in range(len(winners_list)):
#         first_name = winners_list[data].first_name
#         last_name = winners_list[data].last_name
#         prize_name = prizes_list[data].name
#         print(f'{first_name} {last_name} -> {prize_name}')


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
    print_list_of_winners(create_list_of_winners(medal_winners_list, medal_prizes_list))
    # print_list_of_winnersss(medal_winners_list, medal_prizes_list)

    print('xxxxxxxxxxxx')

    item_prizes_list = get_prizes_list(item_giveaway)
    item_winners_list = pick_winners(participants_csv_list, item_prizes_amount)
    print_list_of_winners(create_list_of_winners(item_winners_list, item_prizes_list))
