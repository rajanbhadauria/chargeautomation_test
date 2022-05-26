import pytest

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from utilities.BaseClass import BaseClass

@pytest.mark.usefixtures('loginData')
class TestPaymentRequest(BaseClass):

    # Login to site
    def test_login(self, loginData):
        """Login to charge automation"""
        log = self.myLogger()
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        log.info("Clicking to login link")
        homePage.loginBtn().click()
        log.info("Filling login form")
        loginPage.emailInput().send_keys(loginData['email'])
        log.info("Login email - "+f"'{loginPage.emailInput().get_attribute('value')}'")
        loginPage.passwordInput().send_keys(loginData['password'])
        log.info("Login password - " + f"'{loginPage.passwordInput().get_attribute('value')}'")
        loginPage.loginSubmitBtn().click()



