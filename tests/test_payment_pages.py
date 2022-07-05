import time

import pytest

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.PaymentPagesPage import PaymentPagesPage
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures('loginData')
class TestPaymentPages(BaseClass):

    # Login to site
    def test_login(self, loginData):
        """Test Payment request login to charge automation"""
        log = self.myLogger()
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        paymentPages = PaymentPagesPage(self.driver)
        log.info("Clicking to login link")
        homePage.loginBtn().click()
        log.info("Filling login form")
        loginPage.emailInput().send_keys(loginData['email'])
        log.info("Login email - " + f"'{loginPage.emailInput().get_attribute('value')}'")
        loginPage.passwordInput().send_keys(loginData['password'])
        log.info("Login password - " + f"'{loginPage.passwordInput().get_attribute('value')}'")
        loginPage.loginSubmitBtn().click()
        time.sleep(2)
        log.info("Redirecting manage payment request link")
        paymentPages.paymentPagesLink().click()
        paymentPages.paymentPagesManageLink().click()
        time.sleep(2)

    #create payment page with blank data
    def test_create_payment_page_with_blank_data(self):
        """Creating payment page with blank data"""
        paymentPage = PaymentPagesPage(self.driver)
        log = self.myLogger()
        log.info("Redirecting to create payment page")
        paymentPage.createPaymentPageLink().click()
        time.sleep(2)
        paymentPage.addEditPageSubmitBtn().click()
        product_error_message = paymentPage.productErrorMsg().text
        assert('select product' in product_error_message)
        log.info("Product error message is - "+product_error_message)

    #create product from create payment page with blank data
    #create product with invalid data from create payment page


