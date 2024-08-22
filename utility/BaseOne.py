import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import setup

from selenium.webdriver.support.ui import Select



@pytest.mark.usefixtures("setup")
class BaseClass:

    def test_logger(self):
        filehandler = logging.FileHandler('Logsfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger = logging.getLogger(__name__)
        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)
        logger.debug("A debug statment is executed ")
        logger.info("information statment")
        logger.warning("something is in warning mode")
        logger.error("A major error has happend")
        return logger

    def verifyLinkprensce(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def SelectOptionByText(self,locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)