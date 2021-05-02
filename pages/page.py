import logging

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, WebDriverException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    url = ""

    def __init__(self, driver_instance: WebDriver, content_loc: tuple):
        self.driver = driver_instance
        self.logger = logging.getLogger("page")
        self.content_loc = content_loc

    def wait_until(self, condition, timeout: int = 10, message: str = "Page was not loaded in time"):
        WebDriverWait(self.driver, timeout=timeout,
                      ignored_exceptions=[NoSuchElementException,
                                          StaleElementReferenceException,
                                          AttributeError,
                                          WebDriverException]).until(
            condition,
            message=message,
        )

    def elm_check(self):
        """
        Checks whether the necessary elements are shown on the page.
        :return:
        """
        raise NotImplementedError(f"Element Check not implemented in {self.__class__} page!")

    def wait_for(self, timeout: int = 10, message: str = ""):
        """
        Waits until the page is fully loaded.
        :param timeout: int: timeout in seconds
        :param message: str: log message
        :return:
        """
        if not message:
            message = f"Page {self.__class__} ({self.url}) not loaded in time!"
        self.wait_until(
            lambda x: self.driver.find_element(*self.content_loc).is_displayed(),
            timeout=timeout,
            message=message
        )


