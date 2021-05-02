from selenium.webdriver.chrome.webdriver import WebDriver

from pages.alza_section import AlzaSection
from pages.locators.alza_main_page import LocatorsAlzaMainPage


class MonitorsSection(AlzaSection):
    url = "https://www.alza.cz/luxusni-nejdrazsi-lcd-monitory/18842948.htm"

    def __init__(self,  driver_instance: WebDriver):
        super(AlzaSection, self).__init__(driver_instance=driver_instance,
                                          content_loc=LocatorsAlzaMainPage.MAIN_CONTENT)
