import csv
import json
import random
from pathlib import Path


class Participant:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


def get_file_path(file_name, file_extension):
    data_path = Path('data/').joinpath(file_name + '.' + file_extension)
    return data_path


def load_participants_csv(file_name):
    with open(file_name) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        participants_list = []
        for row in reader:
            participant = Participant(row['id'], row['first_name'], row['last_name'])
            participants_list.append(participant)
        return participants_list


def load_participants_json(file_name):
    with open(file_name) as json_file:
        participants_json = json.load(json_file)
        participants_list = []
        for row in participants_json:
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
    participants = load_participants_csv(get_file_path('participants1', 'csv'))
    json = load_participants_json(get_file_path('participants1', 'json'))
    print_winners(pick_winners(participants, 3))
    print_winners(pick_winners(json, 3))
