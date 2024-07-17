import datetime
import os
import requests

from helper import get_collection, get_refresh_token, set_refresh_token, insert_logger_data

O_AUTH_CODE = 'hTQZpXFv'
REDIRECT_URL = 'https://anodelabs-access.web.app/honeywellsauth'

CLIENT_ID = "AyAFLJTFDycteOBe9qnbAzmtAYNbGBs0"
CLIENT_SECRET = "5frPqTfWgfIbDudM"
AUTHORIZATION_TOKEN = "QXlBRkxKVEZEeWN0ZU9CZTlxbmJBem10QVlOYkdCczA6NWZyUHFUZldnZkliRHVkTQ=="
TOKEN_ENDPOINT = "https://api.honeywell.com/oauth2/token"
HEONEYWELLS_DEVICES_ENDPOINT = 'https://api.honeywell.com/v2/'


def initialize():
    refresh__access_token()


def refresh__access_token():
    now = datetime.datetime.now()
    try:
        payload = {
            'refresh_token': get_refresh_token('honeywells'),
            'grant_type': 'refresh_token'
        }
        headers = {"Authorization": f"Basic {AUTHORIZATION_TOKEN}",
                   "Content-Type": "application/x-www-form-urlencoded"}

        response = requests.post(TOKEN_ENDPOINT, data=payload, headers=headers)
        print(response.text)
        if response.status_code == 200:
            print(response.json())
            access_token = response.json().get('access_token')
            refresh_token = response.json().get('refresh_token')
            set_refresh_token('honeywells', refresh_token)

            list_devices(access_token, now)
        else:
            insert_logger_data('honeywells', False, response.text, now)
    except Exception as e:
        insert_logger_data('honeywells', False, str(e), now)


def list_devices(access_token, now):
    endpoint = f"{HEONEYWELLS_DEVICES_ENDPOINT}locations/?apikey={CLIENT_ID}"
    headers = {"Authorization": f"Bearer {access_token}",
               "Content-Type": "application/json"}
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        print(response.json())
        record_id = dump_data_to_mongodb(response.json())
        insert_logger_data('honeywells', True, f'Data Loaded to mongoDB ({record_id})', now)
    else:
        insert_logger_data('honeywells', False, response.text, now)


def dump_data_to_mongodb(data):
    honeywells_data = get_collection('honeywells')
    record = {
        'data': data,
        'is_processed': False,
        'datetime': datetime.datetime.now()
    }
    record_id = honeywells_data.insert_one(record).inserted_id
    print(record_id)
    return record_id

initialize()
