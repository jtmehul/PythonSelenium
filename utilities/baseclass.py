
import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifylinkPresence(self, textToVerify):

        element = WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located((By.LINK_TEXT, textToVerify)))

    def selectGender(self, locator ,genderText):

        dropDown = Select(locator)
        dropDown.select_by_visible_text(genderText)

    def getlogger(self):

        loggerName= inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filedandler = logging.FileHandler('resources/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filedandler.setFormatter(formatter)
        logger.addHandler(filedandler)  # FileHandler object
        logger.setLevel(logging.INFO)  # Set info level to print only info will be printed in the log file
        return logger