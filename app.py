import csv
import json
from pathlib import Path
from participant import create_participant_list, pick_winners, Participant
from prize import get_prizes_amount, get_prizes_list, Prize


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
    result = list(zip(winners_list, prizes_list))
    return result


def print_list_of_winners(results):
    for data in results:
        first_name = data[0].first_name
        last_name = data[0].last_name
        prize_name = data[1].name
        print(f'{first_name} {last_name} -> {prize_name}')


class CustomEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Participant):
            return f'{obj.first_name} {obj.last_name}'
        elif isinstance(obj, Prize):
            return f'{obj.name}'
        else:
            return json.JSONEncoder.default(self, obj)


def save_result(result, output):
    new = []
    for data in result:
        new.append({'participant': data[0], 'prize': data[1]})
    with open(output, 'w') as f:
        json.dump(new, f, cls=CustomEncoder)


def lottery(output, participant_file, format, prize_file):
    DATA_DIR = Path('data/')
    TEMPLATES_DIR = Path(DATA_DIR / 'lottery_templates/')
    if format == 'json':
        participants_json_raw_data = load_json(DATA_DIR / participant_file)
        participants_list = create_participant_list(data=participants_json_raw_data)

    elif format == 'csv':
        participants_csv_raw_data = load_csv(DATA_DIR / participant_file)
        participants_list = create_participant_list(data=participants_csv_raw_data)

    prizes = load_json(TEMPLATES_DIR / prize_file)
    prizes_amount = get_prizes_amount(prizes)
    prizes_list = get_prizes_list(prizes)
    winners_list = pick_winners(participants_list, prizes_amount)
    create_winners_list = create_list_of_winners(winners_list, prizes_list)
    print_list_of_winners(create_winners_list)
    save_result(create_winners_list, output)


if __name__ == '__main__':
    lottery(participant_file='participants1.json', format='json', prize_file='item_giveaway.json', output='result.json')
