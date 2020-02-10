class Participant:
    def __init__(self, id_, first_name, last_name, weight=1):
        self.id = id_
        self.first_name = first_name
        self.last_name = last_name
        self.weight = weight


def create_participant_list(loaded_file):
    participants_list = []
    for row in loaded_file:
        if 'weight' in row:
            participant = Participant(row['id'], row['first_name'], row['last_name'], row['weight'])
        else:
            participant = Participant(row['id'], row['first_name'], row['last_name'])
        participants_list.append(participant)
    return participants_list


def create_weights_list(participants):
    weight_list = []
    for data in participants:
        weight = data.weight
        weight_list.append(float(weight))
    return weight_list





