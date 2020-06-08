from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR , ".card-title a")
    cardFooter = (By.CSS_SELECTOR , ".card-footer button")
    checkOut = (By.CSS_SELECTOR ,  "a.btn-primary")
    btnfinalcheckout = (By.CSS_SELECTOR , "button.btn-success")
    checkoutProductDetails = (By.XPATH, "//div[@class='card h-100']")
    #self.driver.find_elements_by_xpath("//div[@class='card h-100']")


    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def checkOutItems(self):
        return self.driver.find_element(*CheckoutPage.checkOut)

    def btnfinalco(self):
        self.driver.find_element(*CheckoutPage.btnfinalcheckout).click()
        confpage = ConfirmPage(self.driver)
        return confpage


    def proddetails(self):
        return self.driver.find_elements(*CheckoutPage.checkoutProductDetails)
