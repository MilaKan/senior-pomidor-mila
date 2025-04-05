import json

import pytest
import requests
from constant import BASE_URL

class TestItems:
    item_id = None
    endpoint = f"{BASE_URL}/api/v1/items/"

    def test_post_item(self, item_data, auth_session):
        create_response = auth_session.post(self.endpoint, json=item_data)
        assert create_response.status_code == 200, f"Response: {create_response.status_code}, {create_response.text}"
        self.__class__.item_id = create_response.json().get("id")
        assert self.__class__.item_id is not None,"ID элемента не найдено"
        post_item = create_response.json()
        assert post_item["title"] == item_data["title"],"Заголовок не соответствует"
        assert post_item["description"] == item_data["description"],"Описание не соответствует"

    def test_get_items(self,auth_session):
        get_response = auth_session.get(self.endpoint)
        assert get_response.status_code == 200,"Элементы не найдены"
        assert isinstance(get_response.json().get("data"),list)

    def test_get_item(self,auth_session):
        url = f"{self.endpoint}{self.__class__.item_id}"
        response = auth_session.get(url)
        assert response.status_code == 200,"Элемент не найден"


    def test_put_item(self,item_data,auth_session):
        if not self.__class__.item_id:
            pytest.skip("Необходимо сначала создать элемент")
        url = f"{self.endpoint}{self.__class__.item_id}"
        put_response = auth_session.put(url, json=item_data)
        assert put_response.status_code == 200,"Данные элемента польностью не обновились"
        put_item = put_response.json()
        assert put_item["title"] == item_data["title"],"Заголовок не обновился"
        assert put_item["description"] == item_data["description"],"Описание не обновилось"

    def test_delete_item(self,auth_session):
        if not self.__class__.item_id:
            pytest.skip("Необходимо сначала создать элемент")
        url = f"{self.endpoint}{self.__class__.item_id}"
        delete_response = auth_session.delete(url)
        assert delete_response.status_code == 200,"Элемент не удалён"

    def test_check_delete(self,item_data,auth_session):
        if not self.__class__.item_id:
            pytest.skip("Необходимо сначала создать элемент")
        url = f"{self.endpoint}{self.__class__.item_id}"
        check_response = auth_session.get(url)
        assert check_response.status_code != 200,"Элемент не удалён"

    def test_post_invalid_data(self,auth_session):
        invalid_response = auth_session.post(self.endpoint,json={} )
        assert invalid_response.status_code == 422, "Ожидалась ошибка валидации"

    def test_put_invalid_data(self,auth_session,item_data):
        invalid_response = auth_session.put(f"{self.endpoint}/195",json = item_data)
        assert invalid_response.status_code == 404, "Ожидалась ошибка 'Не найдено'"

    def test_delete_invalid_item(self,item_data,auth_session):
        delete_response = auth_session.delete(f"{self.endpoint}/195")
        assert delete_response.status_code == 404,"Ожидалась ошибка 'Не найдено'"

    def test_unauthorized_access(self, item_data):
        unauth_session = requests.Session()
        response = unauth_session.post(f"{self.endpoint}",json=item_data, headers={"Content-Type": "application/json"})
        assert response.status_code == 401,"Ожидалась ошибка авторизации при создании"