import click

from app import lottery


@click.command()
@click.option("--output", default='result.json', help="Output file name", prompt="Output file name")
@click.option("--participant_file", help="Participants file", prompt="Participants file")
@click.option("--format", default='json', type=click.Choice(['json', 'csv'], case_sensitive=False),
              help="Participant file format", prompt="Participant file format")
@click.option("--prize_file", default='item_giveaway.json', help="Prizes file", prompt="Prizes file")
def main(output, participant_file, format, prize_file):
    lottery(output=output, participant_file=participant_file, format=format, prize_file=prize_file)


if __name__ == '__main__':
    main()
