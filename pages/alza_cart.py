from selenium.webdriver.chrome.webdriver import WebDriver

from pages.locators.alza_cart import LocatorsAlzaCart
from pages.page import Page


class AlzaCart(Page):
    
    def __init__(self, driver_instance: WebDriver):
        super(AlzaCart, self).__init__(driver_instance=driver_instance, content_loc=LocatorsAlzaCart.CART_CONTENT)

    def get_products_in_cart(self) -> list:
        items = self.driver.find_elements(*LocatorsAlzaCart.CART_ITEM_NAME)
        return list(set([item.text for item in items]))  # cast it to set to remove duplicates
