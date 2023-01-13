import logging

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class Base:
    def wait_until(self, by):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(by))

    def test_loggingDemo(self):
        logger = logging.getLogger(__name__)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.INFO)
        return logger
        # logger.debug("A debug statement is executed")
        # logger.info("Information statement")
        # logger.debug("A debug statement is executed")
        # logger.warning("Something is in warning mode")
        # logger.error("A Major error has happend")
        # logger.critical("Critical issue")


