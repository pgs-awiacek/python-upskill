import csv
import json
import random
from pathlib import Path


class Participant:
    def __init__(self, id, first_name, last_name, weight=1):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.weight = weight


def load_participants_csv(file_name):
    with open(file_name) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        data = list(reader)
    return data


def load_participants_json(file_name):
    with open(file_name) as json_file:
        reader = json.load(json_file)
    return reader


def parse_participants(data):
    participants_list = []
    for row in data:
        if 'weight' in row:
            participant = Participant(row['id'], row['first_name'], row['last_name'], row['weight'])
        else:
            participant = Participant(row['id'], row['first_name'], row['last_name'])
        participants_list.append(participant)
    return participants_list


def pick_winners(participants, number):
    winners = random.sample(participants, number)
    return winners


def print_winners(winners):
    print('The winners are: ')
    for name in winners:
        print(name.first_name, name.last_name)


if __name__ == '__main__':
    DATA_DIR = Path('data/')
    participants_raw_data = load_participants_csv(DATA_DIR / 'participants1.csv')
    participants_json_raw_data = load_participants_json(DATA_DIR / 'participants1.json')

    participants_csv_list = parse_participants(data=participants_raw_data)
    participants_json_list = parse_participants(data=participants_json_raw_data)

    print_winners(pick_winners(participants_csv_list, 3))
    print_winners(pick_winners(participants_json_list, 3))
