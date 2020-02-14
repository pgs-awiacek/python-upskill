from pathlib import Path

from app import get_first_lottery_template, pick_winners
from participant import Participant


def test_get_first_lottery_template():
    p = Path().absolute().parent
    test_data = Path(p / 'data/lottery_templates')
    expected = 'item_giveaway.json'

    result = get_first_lottery_template(test_data)
    assert result == expected


class TestPickWinners:

    def test_number_of_winners(self):
        participants = [
            Participant(id_=1, first_name='Aga', last_name='Lamaga', weight=100),
            Participant(id_=2, first_name='Kuba', last_name='Buba', weight=50),
            Participant(id_=3, first_name='Fifi', last_name='Rifi', weight=1)
        ]
        weights = [100, 50, 1]
        amount = 2
        expected = 2
        result = pick_winners(participants, weights, amount)
        assert len(set(result)) == expected

    def test_more_prizes_than_winners(self):
        participants = [
            Participant(id_=1, first_name='Aga', last_name='Lamaga', weight=100),
            Participant(id_=2, first_name='Kuba', last_name='Buba', weight=50),
            Participant(id_=3, first_name='Fifi', last_name='Rifi', weight=1)
        ]
        weights = [100, 50, 1]
        amount = 5
        expected = 3
        result = pick_winners(participants, weights, amount)
        assert len(result) == expected

    def test_zero_participants(self):
        participants = []
        weights = []
        amount = 5
        expected = []
        result = pick_winners(participants, weights, amount)
        assert result == expected

    def test_zero_prizes(self):
        participants = [
            Participant(id_=1, first_name='Aga', last_name='Lamaga', weight=100),
            Participant(id_=2, first_name='Kuba', last_name='Buba', weight=50),
            Participant(id_=3, first_name='Fifi', last_name='Rifi', weight=1)
        ]
        weights = [100, 50, 1]
        amount = 0
        expected = []
        result = pick_winners(participants, weights, amount)
        assert result == expected
