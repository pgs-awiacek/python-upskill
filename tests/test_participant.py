from participant import create_weights_list, Participant, create_participant_list


def test_create_participant_list():
    test_data = [
        {'id': 1, 'first_name': 'Aga', 'last_name': 'Zgaga'},
        {'id': 2, 'first_name': 'Iza', 'last_name': 'Schiza'},
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
