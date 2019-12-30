import csv
import random


def load_participants_csv(file_name):
    with open(file_name) as csv_file:
        # participants_csv = [{data: names for data, names in row.items()}
        #                    for row in csv.DictReader(csv_file, delimiter=',')]
        reader = csv.DictReader(csv_file, delimiter=',')
        participants_list = []
        for row in reader:
            participants_list.append(row)
        return participants_list


# return participants_csv


def pick_winners(number, participants):
    winners_csv = random.sample(participants, number)
    return winners_csv


def print_winners(winners_csv):
    print('The winners are: ')
    for name in winners_csv:
        print(name['first_name'], name['last_name'])


if __name__ == '__main__':
    participants = load_participants_csv('data/participants1.csv')
    # pick_winners(5, participants)
    print_winners(pick_winners(3, participants))
