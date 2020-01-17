class Prize:
    def __init__(self, id_, name, amount):
        self.id = id_
        self.name = name
        self.amount = amount


def get_prizes_amount(file):
    amount_list = []
    for value in file['prizes']:
        amount = value['amount']
        amount_list.append(amount)
    return sum(amount_list)


def get_prizes_list(loaded_file):
    prizes_list = []
    for data in loaded_file['prizes']:
        for _ in range(data['amount']):
            prize = Prize(data['id'], data['name'], data['amount'])
            prizes_list.append(prize)
    return prizes_list
