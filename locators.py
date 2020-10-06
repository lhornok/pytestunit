from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    S_FIELD = (By.NAME, 's')
    ARTICLE_LINK = (By.PARTIAL_LINK_TEXT, 'Coussin')
    ARTICLE_QTY = (By.ID, 'quantity_wanted')
    CART_LINK = (By.XPATH, 'html/body/main/section/div/div/section/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/button')
    CART_DISPLAY_LINK = (By.XPATH, '/html/body/main/header/nav/div/div/div[1]/div[2]/div[3]/div/div/a')
    ARTICLE_QTY_CART = (By.NAME, 'product-quantity-spin')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass
