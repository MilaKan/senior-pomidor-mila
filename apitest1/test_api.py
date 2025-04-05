import pytest
import requests
from constant import BASE_URL,HEADERS

class TestItems:
    item_id = None
    def test_post_item(self, item_data, auth_session):
        create_response = auth_session.post(f"{BASE_URL}/items", json=item_data["post"])
        assert create_response.status_code == 201, "Элемент не создан"
        self.__class__.item_id = create_response.json().get("id")
        assert self.__class__.item_id is not None,"ID элемента не найдено"
        post_item = create_response.json()
        assert post_item["title"] == item_data["post"]["title"],"Заголовок не соответствует"
        assert post_item["description"] == item_data["post"]["description"],"Описание не соответствует"

    def test_get_items(self,auth_session):
        get_response = auth_session.get(f"{BASE_URL}/items")
        assert get_response.status_code == 200,"Элементы не найдены"
        assert isinstance(get_response.json(),list)

    def test_patch_item(self,item_data,auth_session):
        if not self.__class__.item_id:
            pytest.skip("Необходимо сначала создать элемент")
        patch_response = auth_session.patch(f"{BASE_URL}/items/{self.__class__.item_id}", json=["patch"])
        assert patch_response.status_code == 200,"Данные элемента частично не обновились"
        patch_item = patch_response.json()
        assert patch_item["title"] == item_data["patch"]["title"],"Заголовок не обновился"
        assert patch_item["description"] == item_data["patch"]["description"], "Описание изменилось, но не должно было"

    def test_put_item(self,item_data,auth_session):
        if not self.__class__.item_id:
            pytest.skip("Необходимо сначала создать элемент")
        put_response = auth_session.put(f"{BASE_URL}/items/{self.__class__.item_id}", json=["put"])
        assert put_response.status_code == 200,"Данные элемента польностью не обновились"
        put_item = put_response.json()
        assert put_item["title"] == item_data["put"]["title"],"Заголовок не обновился"
        assert put_item["description"] == item_data["put"]["description"],"Описание не обновилось"

    def test_delete_item(self,item_data,auth_session):
        if not self.__class__.item_id:
            pytest.skip("Необходимо сначала создать элемент")
        delete_response = auth_session.delete(f"{BASE_URL}/items/{self.__class__.item_id}")
        assert delete_response.status_code == 200,"Элемент не удалён"

    def test_check_delete(self,item_data,auth_session):
        if not self.__class__.item_id:
            pytest.skip("Необходимо сначала создать элемент")
        check_response = auth_session.get(f"{BASE_URL}/items/{self.__class__.item_id}")
        assert check_response.status_code == 404,"Элемент не удалён"

    def test_post_invalid_data(self,item_data,auth_session):
        invalid_response = auth_session.post(f"{BASE_URL}/items", json=item_data["invalid_data"])
        assert invalid_response.status_code == 422, "Ожидалась ошибка валидации"

    def test_patch_invalid_data(self,auth_session,item_data):
        invalid_response = auth_session.patch(f"{BASE_URL}/items/195",json = item_data["patch"])
        assert invalid_response == 404, "Ожидалась ошибка 'Не найдено'"

    def test_delete_invalid_item(self,item_data,auth_session):
        delete_response = auth_session.delete(f"{BASE_URL}/items/195")
        assert delete_response.status_code == 404,"Ожидалась ошибка 'Не найдено'"

    def test_unauthorized_access(self, item_data):
        unauth_session = requests.session()
        response = unauth_session.post(f"{BASE_URL}/items",json=item_data["post"])
        assert response.status_code == 401,"Ожидалась ошибка авторизации при создании"