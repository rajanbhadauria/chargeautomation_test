import logging
from datetime import datetime, timedelta

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures('setup')
class BaseClass:
    def myLogger(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logger.log')
        # formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        formatter = logging.Formatter("%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def verify_element_presence(self, finder, text):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.finder, text))

    def time_obj(self, add_mins=0):
        return datetime.now() + timedelta(minutes=add_mins)
