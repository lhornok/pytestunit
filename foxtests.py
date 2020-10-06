import unittest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions

import page

import time

class FoxCommand(unittest.TestCase):
    """ test prestashop"""

    def setUp(self):
        self.options = webdriver.FirefoxOptions()
        self.options.set_preference("browser.privatebrowsing.autostart", True)
        self.options.headless=True
        #self.driver = webdriver.Firefox(firefox_options=self.options)
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.get("http://localhost:8002/prestashop/fr/")

    def tests(self):
        """
         - Recherche article Renard
         - Recherche lien coussin
         - Click sur le lien article
         - Affichage du détail de l'article
         - Ajout au panier avec une quantité de 2
         - Affiche du panier 
        """

        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "Title DFTG not found ..."
        main_page.search_text_element = "renard"
        main_page.click_search()
        time.sleep(2)
        main_page.link_article()
        time.sleep(2)
        main_page.put_art_qty()
        time.sleep(2)
        main_page.add_to_cart()
        time.sleep(2)
        main_page.back()
        time.sleep(2)
        main_page.display_cart()
        time.sleep(2)
        assert main_page.check_article_cart(), "Article name not match ..."
        assert main_page.check_article_qty_cart(), "Article quantity not match ..."

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
