from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    SIGNUP_LOGIN = (By.CSS_SELECTOR,"form#login_form input#id_login-username")
    SIGNUP_PASSWORD = (By.CSS_SELECTOR, "form#login_form input#id_login-password")

    REGISTER_EMAIL = (By.CSS_SELECTOR, "form#register_form input#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "form#register_form input#id_registration-password1")
    REGISTER_RE_PASSWORD = (By.CSS_SELECTOR, "form#register_form input#id_registration-password2")

class ProductPageLocators():
    add_to_cart_button = (By.CSS_SELECTOR,"form#add_to_basket_form button")
    alertmsgs = (By.CSS_SELECTOR,"div#messages div.alertinner strong")
    itemname = (By.CSS_SELECTOR,"div.row h1")
    itemprice = (By.CSS_SELECTOR,"div.row p.price_color")
    alertsuccess = (By.CSS_SELECTOR,"div#messages div.alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")