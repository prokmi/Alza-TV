from selenium.webdriver.common.by import By


class LocatorsAlzaMainPage:

    # Main section
    MAIN_CONTENT = (By.CSS_SELECTOR, "#content0")

    # Menu

    # as common as possible so it works in other languages as well
    MENU_MONITORS = (By.CSS_SELECTOR, '.bx > a[href*="lcd-monitor"]')

