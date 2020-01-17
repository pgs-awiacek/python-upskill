import random


class Participant:
    def __init__(self, id_, first_name, last_name, weight=1):
        self.id = id_
        self.first_name = first_name
        self.last_name = last_name
        self.weight = weight


def create_participant_list(data):
    participants_list = []
    for row in data:
        if 'weight' in row:
            participant = Participant(row['id'], row['first_name'], row['last_name'], row['weight'])
        else:
            participant = Participant(row['id'], row['first_name'], row['last_name'])
        participants_list.append(participant)
    return participants_list


def pick_winners(participants, amount):
    winners = random.sample(participants, amount)
    return winners

