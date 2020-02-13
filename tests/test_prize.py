from prize import create_prizes_list


def test_create_prizes_list():
    test_data = {
        'name': 'Prizes list',
        'prizes': [
            {'id': 1, 'name': 'Prize1', 'amount': 1},
            {'id': 2, 'name': 'Prize2', 'amount': 1},
            {'id': 3, 'name': 'Prize3', 'amount': 1}
        ]
    }
    expected = ['Prize1', 'Prize2', 'Prize3']

    result = create_prizes_list(test_data)
    assert [r.name for r in result] == expected
