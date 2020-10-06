from element import BasePageElement
from locators import MainPageLocators
from selenium.webdriver.common.keys import Keys

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 's'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "DFTG" appears in page title"""
        return 'DFTG' in self.driver.title

    def click_search(self):
        element = self.driver.find_element(*MainPageLocators.S_FIELD)
        element.send_keys(Keys.RETURN)

    def link_article(self):
        element = self.driver.find_element(*MainPageLocators.ARTICLE_LINK)
        element.click()

    def put_art_qty(self):
        element = self.driver.find_element(*MainPageLocators.ARTICLE_QTY)
        element.clear()
        element.send_keys('2') 

    def add_to_cart(self):
        element = self.driver.find_element(*MainPageLocators.CART_LINK)
        element.click()

    def display_cart(self):
        element = self.driver.find_element(*MainPageLocators.CART_DISPLAY_LINK)
        element.click()

    def check_article_cart(self):
        element = self.driver.find_element(*MainPageLocators.ARTICLE_LINK)
        return 'Coussin renard' == element.text

    def check_article_qty_cart(self):
        element = self.driver.find_element(*MainPageLocators.ARTICLE_QTY_CART)
        return int(element.get_attribute('value')) == 2

    def back(self):
        self.driver.back()

class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
