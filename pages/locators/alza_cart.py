from selenium.webdriver.common.by import By


class LocatorsAlzaCart:
    CART_CONTENT = (By.CSS_SELECTOR, "div#orderpage")
    BACK_BUTTON = (By.CSS_SELECTOR, "a#varBBackButton")

    CART_ITEM_NAME = (By.CSS_SELECTOR, ".mainItem")
