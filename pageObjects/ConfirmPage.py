
from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element_by_css_selector("#country")
    country = (By.CSS_SELECTOR, "#country")

    selectcountry = (By.LINK_TEXT, "India")
    #self.driver.find_element_by_link_text("India")

    purchase = (By.CSS_SELECTOR, "input.btn-success")
    #self.driver.find_element_by_css_selector("input.btn-success")

    message = (By.CSS_SELECTOR, "div.alert-success")
    #self.driver.find_element_by_css_selector("div.alert-success")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def selectCountry(self):
        return self.driver.find_element(*ConfirmPage.selectcountry)

    def btnpurchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def messageSuccessful(self):
        return self.driver.find_element(*ConfirmPage.message)
