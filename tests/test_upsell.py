import pytest
import time
import re

from selenium.common.exceptions import NoSuchElementException

from pages.UpsellPage import UpsellPage
from utilities.BaseClass import BaseClass
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage

@pytest.mark.usefixtures('loginData')
class TestUpsell(BaseClass):
    # Login to site
    def test_login(self, loginData):
        """Test Payment request login to charge automation"""
        log = self.myLogger()
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        upsellPage = UpsellPage(self.driver)
        log.info("Clicking to login link")
        homePage.loginBtn().click()
        log.info("Filling login form")
        loginPage.emailInput().send_keys(loginData['email'])
        log.info("Login email - " + f"'{loginPage.emailInput().get_attribute('value')}'")
        loginPage.passwordInput().send_keys(loginData['password'])
        log.info("Login password - " + f"'{loginPage.passwordInput().get_attribute('value')}'")
        loginPage.loginSubmitBtn().click()
        time.sleep(2)
        log.info("Redirecting manage upsell page")
        upsellPage.upsellLink().click()
        upsellPage.manageUpsellLink().click()

    # upsell count matching
    def test_upsell_count(self):
        """Match upsell counts"""
        upsellPage = UpsellPage(self.driver)
        log = self.myLogger()
        log.info("Get counts of upsell")
        try:
            upsellCount = re.sub('[^0-9a-zA-Z]+', '', upsellPage.upsellCounts().text)
        except NoSuchElementException:
            upsellCount = 0

        if upsellCount != 0:
            log.info("Total upsell count is as - " + upsellCount)
            maxPage = upsellPage.getAllPages()[-2].text
            log.info("Total page count is - " + maxPage)
            log.info("Loading last page")
            upsellPage.getAllPages()[-2].click()
            time.sleep(2)
            log.info("Counting all upsells in page ")
            totalItems = len(upsellPage.getAllUpsellRowsInPage())
            log.info(f"All upsells in page is {totalItems}")
            log.info("Matching upsell counts")
            total_upsell = ((int(maxPage)-1)*10) + totalItems
            assert total_upsell == int(upsellCount)
            log.info("Upsell count matched")
            log.info(f"Total upsell is - {total_upsell}")
        else:
            log.info("Upsell not found")







    # upsell help link testing
    # create upsell with blank template and blank data
    # create upsell with blank template and invalid data


