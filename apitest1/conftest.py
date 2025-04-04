import pytest
import requests
from faker import Faker
fake = Faker()
from constant import BASE_URL, HEADERS, data

# assert auth_response.status_code == 200, "Токен авторизации не получен"
# assert token is not None, "Токен не получен"

@pytest.fixture(scope="session")
def auth_session():
    session = requests.session()
    auth_response = session.post(f"{BASE_URL}/login/access-token", data=data, headers=HEADERS)
    token = auth_response.json().get("access_token")
    session.headers.update({"Authorization": f"Bearer {token}", "accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"})
    print(session.headers)
    yield session

    # Попытка
    # создать, получить
    # или
    # удалить
    # элемент
    # без
    # токена

@pytest.fixture()
def auth_with_different_ContentType(auth_session):
    return None

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
