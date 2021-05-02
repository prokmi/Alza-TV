from selenium.webdriver.common.by import By


class LocatorsAlzaSection:

    LOADER = (By.CSS_SELECTOR, ".circle-loader-container")

    # Sort buttons
    SORT_TOP_BUTTON = (By.CSS_SELECTOR, "a[href='#alzadoporucuje']")
    SORT_MOST_SOLD_BUTTON = (By.CSS_SELECTOR, "a[href='#nejprodavanejsi']")
    SORT_MOST_EXPENSIVE = (By.CSS_SELECTOR, "a[href='#cenadesc']")
    SORT_LEAST_EXPENSIVE = (By.CSS_SELECTOR, "a[href='#cenaasc']")
    SORT_REVIEWS = (By.CSS_SELECTOR, "a[href='#nejlepehodnocene']")
    SORT_DISCUSSION = (By.CSS_SELECTOR, "a[href='#nejlepehodnocene']")

    # Product elements
    PRODUCT_CONTAINER = (By.CSS_SELECTOR, "div.browsingitem")
    PRODUCT_NAME = (By.CSS_SELECTOR, "a.name")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".priceInner .c2")
    PRODUCT_BUY = (By.CSS_SELECTOR, ".btnk1")
