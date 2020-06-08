import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.baseclass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getlogger()
        log.info("Hello from TestHomePage")
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["firstName"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getPassword().send_keys(getData["password"])
        homePage.getCheckBoxCheck().click()
        self.selectGender(homePage.getGender(), getData["gender"])
        homePage.getSubmitButton().click()
        successMessage = homePage.getAlertMessage().text
        print(successMessage)
        assert "success" in successMessage

    @pytest.fixture(params=HomePageData.test_HomePage_data_dictionary)
    def getData(self, request):
        return request.param



