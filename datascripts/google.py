import datetime

import requests

from helper import get_refresh_token, get_collection, insert_logger_data

O_AUTH_CODE = '4/0AdQt8qh9S6Wm67kFETui1rsc7tKi3wrKo3zo1fgN6bkOk8w5zP4gUE9YozjP3ySdg0cB7w'
REDIRECT_URL = 'https://anodelabs-access.web.app/auth'

CLIENT_ID = "456832363069-rv11ndtvr28m72p997u1mq2na25f8veg.apps.googleusercontent.com"
CLIENT_SECRET = "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"
PROJECT_ID = "0a3886bb-7f3d-46e0-a331-e09e18306cd0"
TOKEN_ENDPOINT = "https://www.googleapis.com/oauth2/v4/token"
GOOGLE_DEVICES_ENDPOINT = 'https://smartdevicemanagement.googleapis.com/v1/enterprises/'


def initialize():
    refresh_token()


def refresh_token():
    now = datetime.datetime.now()
    try:
        payload = {
            'refresh_token': get_refresh_token('google'),
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'grant_type': 'refresh_token'
        }

        response = requests.post(TOKEN_ENDPOINT, json=payload)
        if response.status_code == 200:
            access_token = response.json().get('access_token')
            list_devices(access_token, now)
        else:
            insert_logger_data('google', False, response.text, now)
    except Exception as e:
        insert_logger_data('google', False, str(e), now)


def list_devices(access_token, now):
    endpoint = f"{GOOGLE_DEVICES_ENDPOINT}{PROJECT_ID}/devices"
    headers = {"Authorization": f"Bearer {access_token}",
               "Content-Type": "application/json; charset=UTF-8"}
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        print(response.text)
        record_id = dump_data_to_mongodb(response.json())
        insert_logger_data('google', True, f'Data Loaded to mongoDB ({record_id})', now)
    else:
        insert_logger_data('google', False, response.text, now)


def dump_data_to_mongodb(data):
    google_data = get_collection('google')
    record = {
        'data': data,
        'is_processed': False,
        'datetime': datetime.datetime.now()
    }
    record_id = google_data.insert_one(record).inserted_id
    print(record_id)
    return record_id


initialize()
