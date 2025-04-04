# import requests
# import pytest
#
# from apitest_booking.conftest import auth_session
# from constant import BASE_URL
#
# class TestBooking:
#     def test_create_booking(self,booking_data,auth_session):
#         create_booking = auth_session.post(f"{BASE_URL}/booking",json=booking_data["create"])
#         assert create_booking.status_code == 200,"Бронирование не создано"
#         bookingid = create_booking.json().get("bookingid")
#         assert bookingid is not None,"ID букинга не найден в ответе"
#
#         get_booking = auth_session.get(f"{BASE_URL}/booking/{bookingid}")
#         assert get_booking.status_code == 200
#
#         boooking_data_response = get_booking.json()
#         assert boooking_data_response is not None, "Данные бронирования не найдены в ответе"
#         assert boooking_data_response["firstname"] == booking_data["firstname"], "Имя не совпадает с заданным"
#         assert boooking_data_response["lastname"] == booking_data["lastname"], "Фамилия не совпадает с заданной"
#         assert boooking_data_response["totalprice"] == booking_data["totalprice"], "Цена не совпадает с заданной"
#         assert boooking_data_response["additionalneeds"] == booking_data["additionalneeds"], "Дополнительные потребности не совпадают с заданными"
#
#         patch_booking = auth_session.patch(f"{BASE_URL}/booking/{bookingid}",json=booking_data["patch"])
#         assert patch_booking.status_code == 200,"Бронирование частично не обновлено"
#         boooking_data_response = get_booking.json()
#         assert boooking_data_response is not None, "Данные бронирования не найдены в ответе"
#         assert boooking_data_response["firstname"] == booking_data["firtname"], "Имя не совпадает с заданным"
#         assert boooking_data_response["lastname"] == booking_data["lastname"], "Фамилия не совпадает с заданной"
#         assert boooking_data_response['bookingdates']["checkin"] == booking_data['bookingdates']["checkin"], "Цена не совпадает с заданной"
#         assert boooking_data_response['bookingdates']["checkout"] == booking_data['bookingdates']["checkout"], "Дополнительные потребности не совпадают с заданными"
#
#         put_booking = auth_session().put(f"{BASE_URL}/booking/{bookingid}", json = booking_data["put"])
#         assert put_booking.status_code == 400, "Бронирование не обновлено полностью"
#         boooking_data_response = get_booking.json()
#         assert boooking_data_response is not None, "Данные бронирования не найдены в ответе"
#         assert boooking_data_response["firstname"] == booking_data["firstname"], "Имя не совпадает с заданным"
#         assert boooking_data_response["lastname"] == booking_data["lastname"], "Фамилия не совпадает с заданной"
#         assert boooking_data_response["totalprice"] == booking_data["totalprice"], "Цена не совпадает с заданной"
#         assert boooking_data_response["additionalneeds"] == booking_data["additionalneeds"], "Дополнительные потребности не совпадают с заданными"
#         assert boooking_data_response['bookingdates']["checkin"] == booking_data['bookingdates']["checkin"], "Цена не совпадает с заданной"
#         assert boooking_data_response['bookingdates']["checkout"] == booking_data['bookingdates']["checkout"], "Дополнительные потребности не совпадают с заданными"
#         assert boooking_data_response["depositpaid"] == True, "Депозит был отменён"
#
#         delete_booking = auth_session.delete(f"{BASE_URL}/booking/{bookingid}")
#         assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {bookingid}"
#
#         check_delete_booking = auth_session.get(f"{BASE_URL}/booking/{bookingid}")
#         assert check_delete_booking.status_code == 404, f"Букинг с ID {bookingid} не был удален"

