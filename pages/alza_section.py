import enum

from selenium.webdriver import ActionChains

from pages.locators.alza_cart import LocatorsAlzaCart
from pages.locators.alza_section import LocatorsAlzaSection
from pages.page import Page


class AlzaSection(Page):
    url = ""

    class SortTypes(enum.Enum):
        TOP = LocatorsAlzaSection.SORT_TOP_BUTTON
        MOST_SOLD = LocatorsAlzaSection.SORT_MOST_SOLD_BUTTON
        MOST_EXPENSIVE = LocatorsAlzaSection.SORT_MOST_EXPENSIVE
        LEAST_EXPENSIVE = LocatorsAlzaSection.SORT_LEAST_EXPENSIVE
        REVIEWS = LocatorsAlzaSection.SORT_REVIEWS
        DISCUSSION = LocatorsAlzaSection.SORT_DISCUSSION

    def sort_by(self, category: SortTypes):
        """
        Selects the sort type, clicks on the button and waits until it's loaded
        :param category: SortTypes: selected type of sorting
        :return:
        """
        category_elm = self.driver.find_element(*category.value)
        ActionChains(self.driver).move_to_element(category_elm).perform()
        category_elm.click()
        ActionChains(self.driver).move_to_element(category_elm).perform()  # scroll back
        # wait until the loader disappears and the tab is active
        self.wait_until(
            lambda x: not self.driver.find_element(*LocatorsAlzaSection.LOADER).is_displayed()
            and "ui-tabs-active" in category_elm.find_element_by_xpath("..").get_attribute("class"),
            10,
            "Category wasn't switched in time"
        )

    def get_products_on_page(self) -> list:
        self.logger.debug("Getting products no the page..")
        elements = self.driver.find_elements(*LocatorsAlzaSection.PRODUCT_CONTAINER)
        products = []
        unique_names = []
        for element in elements:
            ActionChains(self.driver).move_to_element(element)
            product = {"elm": element,
                       "name": element.find_element(*LocatorsAlzaSection.PRODUCT_NAME).text,
                       "price": int(element.find_element(*LocatorsAlzaSection.PRODUCT_PRICE).text.replace(",-", "").replace(" ", "")),
                       "buy_btn": element.find_element(*LocatorsAlzaSection.PRODUCT_BUY)}
            # only append when the elm doesnt exist:
            if product["name"] not in unique_names:
                # easier than parsing dict in lists
                products.append(product)
                unique_names.append(product["name"])
        self.logger.debug(f"Following products found: {unique_names}")
        return products

    def add_product(self, product):
        self.logger.debug(f"Adding product {product['name']} to cart..")
        product["buy_btn"].click()
        self.wait_until(
            lambda x:  self.driver.find_element(*LocatorsAlzaCart.BACK_BUTTON).is_displayed(),
            10,
            "Back button wasn't loaded in time"
        )
        self.driver.find_element(*LocatorsAlzaCart.BACK_BUTTON).click()
        self.wait_for()

    def _get_sorted_products(self) -> list:
        products = self.get_products_on_page()

        def price_sort(e):
            return e["price"]

        products.sort(reverse=True, key=price_sort)
        return products

    def add_most_expensive_products(self, number) -> list:

        added = []

        while len(added) < number:
            products = self._get_sorted_products()
            for product in products:
                if product["name"] not in added:
                    self.add_product(product)
                    added.append(product["name"])
                    break
        return added
