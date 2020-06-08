import time
import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.baseclass import BaseClass


class TestHomePage(BaseClass):
    def test_end2end(self):
        log = self.getlogger()
        homepage = HomePage(self.driver)
        cop = homepage.shopItems()
        log.info("getting all card details")
        #cop = CheckoutPage(self.driver)
        products = cop.proddetails()
        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            if productName == "Blackberry":
                # Add item to the cart
                log.info("Product names")
                product.find_element_by_xpath("div/button").click()
        cop.checkOutItems().click()
        confpage = cop.btnfinalco()
        confpage = ConfirmPage(self.driver)
        confpage.getCountry().send_keys("Ind")
        self.verifylinkPresence("India")

        confpage.selectCountry().click()
        # driver.find_element_by_css_selector("#checkbox2").click()
        confpage.btnpurchase().click()
        alertSuccess = confpage.messageSuccessful().text
        log.info(alertSuccess)
        assert "Success! Thank you!" in alertSuccess
        x = datetime.datetime.now()
        now = x.strftime('%m/%d/%Y')
        log.info(now)
        self.driver.get_screenshot_as_file("resources/screenshot.png")
