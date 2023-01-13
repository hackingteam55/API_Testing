import requests
from random import randint


def login(client_name=None, client_email=None):
    json = {
        'clientName': client_name,
        'clientEmail': client_email
    }
    response = requests.post('https://simple-books-api.glitch.me/api-clients/', json=json)
    return response
    # la login ce se intampla in "spate" e ca se trimite un json
    # ne definim json-ul pe care vrem sa il trimitem


def get_token():
    nr = randint(1, 9999999)
    json = {
        'clientName': 'Marin',
        'clientEmail': f'valid_email{nr}@email.com'
    }
    response = requests.post('https://simple-books-api.glitch.me/api-clients/', json=json)
    return response.json()['accessToken']

    # in functia get_token ne definim o adresa random de email
    # ca sa ne putem loga de fiecare data cand rulam acest test
    # in urma trimiterii numelui + adresei de email vom primi un token
    # care il primim la linia 23  in return


def invalid_login(client_name=None):
    invalid_json = {
        'clientName': client_name,
    }
    response = requests.post('https://simple-books-api.glitch.me/api-clients/', json=invalid_json)
    return response

