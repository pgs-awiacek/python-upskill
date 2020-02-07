from participant import create_weights_list, Participant, pick_winners, create_participant_list


def test_create_participant_list():
    test_data = [
        {'id': 1, 'first_name': 'Aga', 'last_name': 'Zgaga'},
        {'id': 2, 'first_name': 'Ada', 'last_name': 'Bada'},
        {'id': 3, 'first_name': 'Ola', 'last_name': 'Fasola'}
    ]
    expected = [1.0, 1.0, 1.0]

    result = create_participant_list(test_data)
    assert [r.weight for r in result] == expected


def test_create_weight_list():
    test_data = [
        Participant(id_="1", first_name='Aga', last_name='Lamaga', weight=2),
        Participant(id_="2", first_name='Kuba', last_name='Buba', weight=3),
        Participant(id_="3", first_name='Fifi', last_name='Rifi', weight=5)
    ]
    expected = [2.0, 3.0, 5.0]

    result = create_weights_list(test_data)
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
