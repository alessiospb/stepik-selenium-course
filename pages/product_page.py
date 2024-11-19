from .base_page import BasePage
from .locators import ProductPageLocators
import time
class ProductPage(BasePage):

    def get_item_data(self):
        assert self.is_element_present(*ProductPageLocators.itemname), "Item name not found"
        assert self.is_element_present(*ProductPageLocators.itemprice), "Item price not found"
        name = self.find_element(*ProductPageLocators.itemname).text
        price = self.find_element(*ProductPageLocators.itemprice).text
        return name,price

    def add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.add_to_cart_button),"No add to cart button"
        self.find_element(*ProductPageLocators.add_to_cart_button).click()
        self.solve_quiz_and_get_code()
        #time.sleep(5)

    def check_item_added(self,name,price):
        assert self.is_element_present(*ProductPageLocators.alertmsgs), "No alerts at all"
        alert_msgs = self.find_elements(*ProductPageLocators.alertmsgs)
        flag = 0
        for am in alert_msgs:

            if am.text == name:
                flag += 1
            if am.text == price:
                flag += 1

        assert flag == 2 , "Not all success messages exists: "+str(flag)




