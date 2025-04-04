from checkout_order.checkout_page import CheckoutPage
from checkout_order.conftest import browser
from checkout_order.inventory_page import InventoryPage
from checkout_order.login_page import LoginPage

# def test_checkout_order1(page):
#     print("Current URL:", page.url)  # Проверяем где находимся
#     print("Page content:", page.content()[:1000])  # Смотрим первые 1000 символов HTML
#     checkout_page = CheckoutPage(page)
#     # ...
def test_checkout_order(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout("Mila","Kan","12345")
    checkout_page.contain_checkout()
    checkout_page.finish_checkout()
    checkout_page.burger_button()
    checkout_page.logout_button()