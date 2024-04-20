import requests
import logging

log = logging.getLogger('django')


def check_password(series, number):
    data = {
        'serial': series,
        'number': number,
    }

    rsp = requests.post('https://proverk.ru/ajax.php', data=data)
    data = rsp.json()
    log.warning(rsp.text)
    return data['passport_serial'].startswith('60') and data['result'] == 'valid'
