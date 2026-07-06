import random
import string

import requests

from data import UserData
from urls import Urls


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


def generate_user_data():
    return {
        "email": f"{generate_random_string()}@yandex.ru",
        "password": UserData.PASSWORD,
        "name": UserData.NAME,
    }


def create_user():
    user_data = generate_user_data()
    response = requests.post(Urls.CREATE_USER, json=user_data)
    access_token = response.json()["accessToken"]
    return user_data, access_token


def delete_user(access_token):
    requests.delete(
        Urls.DELETE_USER,
        headers={"Authorization": access_token}
    )