from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Current url doesn't contain substring 'login'"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGNUP_LOGIN), "Signup login field not found"
        assert self.is_element_present(*LoginPageLocators.SIGNUP_PASSWORD), "Signup password field not found"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Register email field not found"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "Register password field not found"
        assert self.is_element_present(*LoginPageLocators.REGISTER_RE_PASSWORD), "Register repeat password field not found"
