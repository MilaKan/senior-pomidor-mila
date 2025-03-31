import pytest
import requests
from faker import Faker
fake = Faker()
from constant import BASE_URL ,HEADERS


@pytest.fixture(scope = "session")
def auth_session():
    session = requests.session()
    auth_data = {
        "grant_type": "password",
        "username": "Kan@mail.ru",
        "password": "Kan@mail.ru",
        "scope": "",
        "client_id": "string",
        "client_secret": "string"
    }
    auth_url = f"{BASE_URL}/login/access-token"
    try:
        # Добавляем логирование для отладки
        print(f"\nAuth URL: {auth_url}")
        print(f"Auth data: {auth_data}")

        auth_response = session.post(auth_url,data = auth_data, headers=HEADERS)
        assert auth_response.status_code == 200,"Токен авторизации не получен"
        print(f"Auth response: {auth_response.status_code}, {auth_response.text}")

        if auth_response.status_code != 200:
            pytest.fail(f"Auth failed: {auth_response.status_code} - {auth_response.text}")


        token = auth_response.json().get("access_token")
        assert token is not None, "Токен не получен"

        session.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "accept": "application/json"
        })
        print("\nSession headers:", session.headers)
        return session

    except Exception as e:
        pytest.fail(f"Auth error: {str(e)}")




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