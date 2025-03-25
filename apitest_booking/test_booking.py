import requests
import pytest

from apitest_booking.conftest import auth_session
from constant import BASE_URL

class TestBooking:
    def test_create_booking(self,booking_data,auth_session):
        create_booking = auth_session.post(f"{BASE_URL}/booking",json=booking_data["create"])
        assert create_booking.status_code == 200,"Бронирование не создано"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None,"ID букинга не найден в ответе"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        boooking_response = get_booking.json()
        assert boooking_response is not None, "Данные бронирования не найдены в ответе"
        for field in booking_data["create"]:
            if field == "bookingdates":
                for date_field in booking_data["create"]["bookingdates"]:
                    assert boooking_response["bookingdates"][date_field] == booking_data["create"]["bookingdates"][date_field],f"Дата {date_field} не совпадает"
            else:
                assert boooking_response[field] == booking_data["create"][field],f"Поле {field} не совпадает"

        patch_booking = auth_session.patch(f"{BASE_URL}/booking/{booking_id}",json=booking_data["patch"])
        assert patch_booking.status_code == 200,"Бронирование частично не обновлено"
        patch_response = auth_session.patch(f"{BASE_URL}/booking/{booking_id}",json=booking_data["patch"])
        assert patch_response.status_code == 200, "Ошибка частичного обновления"

        get_patched = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        patched_data = get_patched.json()
        assert patched_data is not None, "Обновленные данные не найдены"
        for field in booking_data["patch"]:
            if field == "bookingdates":
                for date_field in booking_data["patch"]["bookingdates"]:
                    assert patched_data["bookingdates"][date_field] == booking_data["patch"]["bookingdates"][date_field], f"Дата {date_field} не обновилась"
            else:
                assert patched_data[field] == booking_data["patch"][field], f"Поле {field} не обновилось"
        put_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json = booking_data["put"])
        assert put_booking.status_code == 200, "Бронирование не обновлено полностью"
        get_put = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        put_data = get_put.json()
        assert put_data is not None, "Данные бронирования не найдены в ответе"
        for field in booking_data["put"]:
            if field == "bookingdates":
                for date_field in booking_data["put"]["bookingdates"]:
                    assert put_data["bookingdates"][date_field] == booking_data["put"]["bookingdates"][date_field], f"Дата {date_field} не обновилась"
            else:
                assert put_data[field] == booking_data["put"][field], f"Поле {field} не обновилось"
        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        check_delete_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert check_delete_booking.status_code == 404, f"Букинг с ID {booking_id} не был удален"