import csv
import json
from pathlib import Path
from participant import create_participant_list, pick_winners, Participant, create_weights_list
from prize import get_prizes_amount, get_prizes_list, Prize
import click
import sys


def load_csv(path):
    try:
        with open(path) as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            data = list(reader)
        return data
    except FileNotFoundError:
        sys.exit(f'Error: No such file or directory: {path}')


def load_json(path):
    try:
        with open(path) as json_file:
            reader = json.load(json_file)
        return reader
    except FileNotFoundError:
        sys.exit(f'Error: No such file or directory: {path}')


def get_first_template(files):
    templates_list = []
    for file in files.iterdir():
        temp_name = file.name
        templates_list.append(temp_name)
    return templates_list[0]


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


@click.command()
@click.option("--output", default='result.json', help="Output file name")
@click.argument("participant_file")
@click.option("--file_format", default='json', type=click.Choice(['json', 'csv'], case_sensitive=False),
              help="Participant file format")
@click.option("--prize_file", default=None, help="Prizes file")
def lottery(output, participant_file, file_format, prize_file):
    if file_format == 'json':
        participants_json_raw_data = load_json(DATA_DIR / participant_file)
        participants_list = create_participant_list(data=participants_json_raw_data)
    elif file_format == 'csv':
        participants_csv_raw_data = load_csv(DATA_DIR / participant_file)
        participants_list = create_participant_list(data=participants_csv_raw_data)
    else:
        raise Exception('Invalid file format')

    if prize_file is None:
        first_template = get_first_template(TEMPLATES_DIR)
        prizes = load_json(TEMPLATES_DIR / first_template)
    else:
        prizes = load_json(TEMPLATES_DIR / prize_file)

    prizes_amount = get_prizes_amount(prizes)
    prizes_list = get_prizes_list(prizes)
    weights_list = create_weights_list(participants_list)
    winners_list = pick_winners(participants_list, weights_list, prizes_amount)
    create_winners_list = create_list_of_winners(winners_list, prizes_list)
    print_list_of_winners(create_winners_list)
    if Path(output).suffix == '.json':
        save_result(create_winners_list, output)
    else:
        suffix = '.json'
        output += suffix
        save_result(create_winners_list, output)
    # click.launch("result.json")


if __name__ == '__main__':
    DATA_DIR = Path('data/')
    TEMPLATES_DIR = Path(DATA_DIR / 'lottery_templates/')
    lottery()
