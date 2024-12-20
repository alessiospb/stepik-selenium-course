import time
import pytest
from .pages.locators import ProductPageLocators
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage




@pytest.mark.xfail(reason="this test should fail")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    (itemname, itemprice) = page.get_item_data()
    page.add_to_cart()
    time.sleep(5)
    assert page.is_not_element_present(*ProductPageLocators.alertsuccess),"Guest can see success message"




@pytest.mark.xfail(reason="this test should fail")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    (itemname, itemprice) = page.get_item_data()
    page.add_to_cart()
    assert page.is_disappeared(*ProductPageLocators.alertsuccess),"Message not disappered"


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.check_link_to_basket_exists()
    page.check_basket_is_empty()
    page.check_that_there_areno_items_in_basket()

def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    (itemname, itemprice) = page.get_item_data()
    # time.sleep(60)
    assert page.is_not_element_present(*ProductPageLocators.alertsuccess), "Guest can see success message"

@pytest.mark.need_review
@pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param(
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
     page = ProductPage(browser, link)
     page.open()
     (itemname, itemprice) = page.get_item_data()
     page.add_to_cart()
#     time.sleep(5)
     page.check_item_added(itemname, itemprice)

class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.should_be_login_link()
        page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email,str(time.time()))
        page.should_be_authorized_user()



    def test_user_cant_see_success_message(self,browser):
        link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        (itemname, itemprice) = page.get_item_data()
        # time.sleep(60)
        assert page.is_not_element_present(*ProductPageLocators.alertsuccess), "Guest can see success message"

    @pytest.mark.need_review
    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param(
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_user_can_add_product_to_basket(self, browser, link):
        # product_page_url = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        # product_page_url = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        (itemname, itemprice) = page.get_item_data()
        page.add_to_cart()
        time.sleep(5)
        page.check_item_added(itemname, itemprice)




