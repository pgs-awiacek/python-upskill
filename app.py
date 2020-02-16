import csv
import json
import random
from pathlib import Path
import click
import sys
from participant import Participant, create_participant_list, create_weights_list
from prize import Prize, create_prizes_list


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


def get_first_lottery_template(files):
    templates_list = []
    for file in files.iterdir():
        temp_name = file.name
        templates_list.append(temp_name)
    return templates_list[0]


def pick_winners(participants, weights, prizes_amount):
    winners = []
    if len(participants) >= prizes_amount:
        while len(set(winners)) < prizes_amount:
            winners = random.choices(participants, weights=weights, k=prizes_amount)
    elif len(participants) < prizes_amount:
        winners = participants
    return winners


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


def prepare_result(winners_list):
    results_list = [{'participant': data[0], 'prize': data[1]} for data in winners_list]
    return results_list


def save_result(result, output_file):
    with open(output_file, 'w') as f:
        json.dump(result, f, cls=CustomEncoder)


def select_participants_file(file_format, participant_file):
    if file_format == 'json':
        participants_json_raw_data = load_json(DATA_DIR / participant_file)
        participants_list = create_participant_list(loaded_file=participants_json_raw_data)
    elif file_format == 'csv':
        participants_csv_raw_data = load_csv(DATA_DIR / participant_file)
        participants_list = create_participant_list(loaded_file=participants_csv_raw_data)
    else:
        raise Exception('Invalid file format')
    return participants_list


def select_prize_file(prize_file):
    if prize_file is None:
        first_template = get_first_lottery_template(TEMPLATES_DIR)
        prizes = load_json(TEMPLATES_DIR / first_template)
    else:
        prizes = load_json(TEMPLATES_DIR / prize_file)
    return prizes


def save_result_file(output, prepared_result):
    if Path(output).suffix == '.json':
        save_result(prepared_result, output)
    else:
        suffix = '.json'
        output += suffix
        save_result(prepared_result, output)


@click.command()
@click.option("--output", default='result.json', help="Output file name")
@click.argument("participant_file")
@click.option("--file_format", default='json', type=click.Choice(['json', 'csv'], case_sensitive=False),
              help="Participant file format")
@click.option("--prize_file", default=None, help="Prizes file")
def main(output, participant_file, file_format, prize_file):
    participants_list = select_participants_file(file_format, participant_file)

    prizes = select_prize_file(prize_file)
    prizes_list = create_prizes_list(prizes)

    prizes_amount = len(prizes_list)
    weights_list = create_weights_list(participants_list)
    picked_winners = pick_winners(participants_list, weights_list, prizes_amount)
    winners_with_prizes = list(zip(picked_winners, prizes_list))

    print_list_of_winners(winners_with_prizes)
    prepared_result = prepare_result(winners_with_prizes)
    save_result_file(output, prepared_result)


if __name__ == '__main__':
    DATA_DIR = Path('data/')
    TEMPLATES_DIR = Path(DATA_DIR / 'lottery_templates/')
    main()
