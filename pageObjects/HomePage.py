from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.XPATH, "//input[@type='password']")
    check = (By.ID, "exampleCheck1")
    genderS = (By.ID, "exampleFormControlSelect1")
    sub = (By.XPATH, "//input[@value='Submit']")
    txt = (By.CLASS_NAME, "alert-success")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        cop = CheckoutPage(self.driver)
        return cop

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckBoxCheck(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.genderS)

    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.sub)

    def getAlertMessage(self):
        return self.driver.find_element(*HomePage.txt)




