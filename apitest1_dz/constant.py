BASE_URL = "https://api.pomidor-stage.ru"
LOGIN_URL = f"{BASE_URL}/api/v1/login/access-token"
ITEMS_URL = f"{BASE_URL}/api/v1/items/"

AUTH_HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}

API_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

AUTH_DATA = {
    "username": "kan@mail.ru",
    "password": "kan@mail.ru",
    "scope": "",
    "client_id": "",
    "client_secret": ""
}