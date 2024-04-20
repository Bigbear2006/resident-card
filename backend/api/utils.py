import random
import string

import requests


def check_password(series, number):
    data = {
        'serial': series,
        'number': number,
    }

    rsp = requests.post('https://proverk.ru/ajax.php', data=data)
    data = rsp.json()

    if data['result'] == 'error':
        return False
    return data['passport_serial'].startswith('60') and data['result'] == 'valid'


def make_card_number():
    return int(''.join(random.choices(string.digits, k=16)))


def make_cvv():
    return int(''.join(random.choices(string.digits, k=3)))
