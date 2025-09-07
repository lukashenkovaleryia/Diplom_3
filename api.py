import requests
from data import Urls


def create_user_request(payload):
    response = requests.post(Urls.REGISTRATION_URL, data=payload)
    return response.json()

def delete_user_request(headers):
    response = requests.delete(Urls.DELETE_USER_URL, headers=headers)
    return response.json()
