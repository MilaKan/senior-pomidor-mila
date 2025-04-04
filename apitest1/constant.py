BASE_URL = "https://api.pomidor-stage.ru/api/v1"
HEADERS = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "password",
    "username": "kan@mail.ru",
    "password": "kan@mail.ru"
    }

put_update_data = {

  "title": "updated_title",
  "description": "updated_description"
}