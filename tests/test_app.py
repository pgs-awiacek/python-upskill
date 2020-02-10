from pathlib import Path

from app import get_first_lottery_template, create_list_of_winners, pick_winners
from participant import Participant
from prize import Prize


def test_get_first_lottery_template():
    p = Path().absolute().parent
    test_data = Path(p / 'data/lottery_templates')
    expected = 'item_giveaway.json'

    result = get_first_lottery_template(test_data)
    assert result == expected


def test_pick_winners():
    participants = [
        Participant(id_="1", first_name='Aga', last_name='Lamaga', weight=100),
        Participant(id_="2", first_name='Kuba', last_name='Buba', weight=50),
        Participant(id_="3", first_name='Fifi', last_name='Rifi', weight=1)
    ]
    weights = [100, 50, 1]
    amount = 2
    expected = ["1", "2"]
    result = pick_winners(participants, weights, amount)
    assert sorted([r.id for r in result]) == expected


def test_create_list_of_winners():
    test_winners = [
        Participant(id_="1", first_name='Aga', last_name='Lamaga', weight=2),
        Participant(id_="2", first_name='Kuba', last_name='Buba', weight=3),
        Participant(id_="3", first_name='Fifi', last_name='Rifi', weight=5)
    ]
    test_prizes = [
        Prize(id_="1", name='Prize1', amount='1'),
        Prize(id_="2", name='Prize2', amount='1'),
        Prize(id_="3", name='Prize3', amount='1'),
    ]
    expected = ['Aga', 'Kuba', 'Fifi'] and ['Lamaga', 'Buba', 'Rifi'] and ['Prize1', 'Prize2', 'Prize3']

    result = create_list_of_winners(test_winners, test_prizes)
    assert [fn[0].first_name for fn in result] and [ln[0].last_name for ln in result] and [p[1].name for p in
                                                                                           result] == expected
