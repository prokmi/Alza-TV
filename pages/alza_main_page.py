
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.alza_sections.monitors_section import MonitorsSection
from pages.locators.alza_main_page import LocatorsAlzaMainPage
from pages.page import Page


class AlzaMainPage(Page):
    url = "https://www.alza.cz/"

    def __init__(self,  driver_instance: WebDriver):
        super(AlzaMainPage, self).__init__(driver_instance=driver_instance,
                                           content_loc=LocatorsAlzaMainPage.MAIN_CONTENT)
        self.menu_sections = {
            "monitors": (LocatorsAlzaMainPage.MENU_MONITORS, MonitorsSection),
            # more can be added
        }

    def open_section(self, section_name: str):
        selected_section = self.menu_sections.get(section_name)
        if not selected_section:
            raise ValueError("Unknown section selected!")

        self.driver.find_element(*selected_section[0]).click()
        return selected_section[1](driver_instance=self.driver)
