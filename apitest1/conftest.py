import pytest
import requests
from faker import Faker
fake = Faker()
from constant import BASE_URL, HEADERS


@pytest.fixture(scope = "session")
def auth_session():
    session = requests.session()
    session.headers.update(HEADERS)
    auth_data = {"email": "Bulanbekova01@mail.ru", "password": "123456789"}
    auth_url = f"{BASE_URL}/api/v1/login/access-token"
    auth_response = requests.post(auth_url, json=auth_data)
    assert auth_response.status_code == 200,"Токен авторизации не получен"

    token = auth_response.json().get("token")
    assert token is not None, "Токен не получен"

    session.headers.update({"Authorization":f"Bearer: {token}"})
    return session

@pytest.fixture()
def item_data():
    post_data = {
        "title": fake.sentence(nb_words=3),
        "description": fake.text(max_nb_chars=200)
    }

    patch_data = {
        "title": fake.sentence(nb_words=2),
        "description": fake.text(max_nb_chars=100)
    }

    put_data = {
        "title": fake.sentence(nb_words=4),
        "description": fake.text(max_nb_chars=300)
    }
    invalid_data = {
        "title": "",
        "description": ""
    }
    return {
        "post": post_data,
        "patch": patch_data,
        "put": put_data,
        "post_invalid_data": invalid_data
    }
