from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.XPATH,"//span[contains(@class, 'btn-group')]//a[contains(@href, 'basket') and contains(@class, 'btn btn-default')]")

class BasketPageLocators():
    ITEM_IN_BASKET = (By.CSS_SELECTOR,"div.basket-items")
    EMPTY_BASKET_RU = (By.XPATH,"//p[contains(text(), 'Ваша корзина пуста')]")
    EMPTY_BASKET_EN = (By.XPATH,"//p[contains(text(), 'Your basket is empty')]")

class LoginPageLocators():
    SIGNUP_LOGIN = (By.CSS_SELECTOR,"form#login_form input#id_login-username")
    SIGNUP_PASSWORD = (By.CSS_SELECTOR, "form#login_form input#id_login-password")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "form#login_form button")


    REGISTER_EMAIL = (By.CSS_SELECTOR, "form#register_form input#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "form#register_form input#id_registration-password1")
    REGISTER_RE_PASSWORD = (By.CSS_SELECTOR, "form#register_form input#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "form#register_form button")

class ProductPageLocators():
    add_to_cart_button = (By.CSS_SELECTOR,"form#add_to_basket_form button")
    alertmsgs = (By.CSS_SELECTOR,"div#messages div.alertinner strong")
    itemname = (By.CSS_SELECTOR,"div.row h1")
    itemprice = (By.CSS_SELECTOR,"div.row p.price_color")
    alertsuccess = (By.CSS_SELECTOR,"div#messages div.alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")