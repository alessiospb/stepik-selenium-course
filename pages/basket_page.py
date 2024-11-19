from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BasketPageLocators
class BasketPage(BasePage):



    def check_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_RU) or self.is_element_present(*BasketPageLocators.EMPTY_BASKET_EN), "'Empty basket' message not found"

    def check_that_there_areno_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET),"Items found in basket cinsudered as empty"