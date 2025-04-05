import pytest
import requests
from faker import Faker

from apitest1_dz.constant import AUTH_DATA, BASE_URL, AUTH_HEADERS , API_HEADERS

fake = Faker()


# assert auth_response.status_code == 200, "Токен авторизации не получен"
# assert token is not None, "Токен не получен"

@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    auth_response = session.post(f"{BASE_URL}/api/v1/login/access-token", data=AUTH_DATA, headers=AUTH_HEADERS)
    assert auth_response.status_code == 200, "Токен авторизации не получен"
    token = auth_response.json().get("access_token")
    assert token is not None, "Токен не получен"
    session.headers.update(API_HEADERS)
    session.headers.update({"Authorization": f"Bearer {token}"})

    return session


@pytest.fixture()
def auth_with_different_ContentType(auth_session):
    return None

@pytest.fixture()
def item_data():
    return {
         "title": fake.word(),
         "description": fake.text()
        }


# def item_data():
#     post_data = {
#         "title": fake.sentence(nb_words=3),
#         "description": fake.text(max_nb_chars=200)
#     }
#
#     # patch_data = {
#     #     "title": fake.sentence(nb_words=2),
#     #     "description": fake.text(max_nb_chars=100)
#     # }
#
#     put_data = {
#         "title": fake.sentence(nb_words=4),
#         "description": fake.text(max_nb_chars=300)
#     }
#     invalid_data = {
#         "title": "",
#         "description": ""
#     }
#     return {
#         "post": post_data,
#         "put": put_data,
#         "post_invalid_data": invalid_data
#     }
#
#
# # "patch": patch_data,