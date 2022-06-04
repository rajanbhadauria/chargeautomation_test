import time,  datetime

import pytest
from faker import Faker

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.PaymentRequestPage import PaymentRequestPage
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures('loginData')
class TestPaymentRequest(BaseClass):

    # Login to site
    def test_login(self, loginData):
        """Test Payment request login to charge automation"""
        log = self.myLogger()
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        paymentRequestPage = PaymentRequestPage(self.driver)
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
        paymentRequestPage.paymentRequestLink().click()
        paymentRequestPage.managePaymentRequestLink().click()
        time.sleep(2)

    # Test create payment request with blank data
    def test_create_payment_request_with_blank_data(self):
        """Test create payment request with blank data"""
        log = self.myLogger()
        paymentRequestPage = PaymentRequestPage(self.driver)
        paymentRequestPage.addPaymentRequestLink().click()
        log.info("Submit form with blank data")
        paymentRequestPage.amountInput().clear()
        paymentRequestPage.sendPaymentRequest().click()
        time.sleep(2)
        log.info("Email validation message " + f"'{paymentRequestPage.emailError().text}'")
        assert ('email field is required' in paymentRequestPage.emailError().text)
        log.info("Email validation message " + f"'{paymentRequestPage.amountError().text}'")
        assert ('amount must be at least 1' in paymentRequestPage.amountError().text)

    # Test create payment request with invalid email and amount
    def test_create_payment_request_with_invalid_data(self):
        """Test create payment request with invalid email and amount"""
        log = self.myLogger()
        paymentRequestPage = PaymentRequestPage(self.driver)

        log.info("Filling email ")
        paymentRequestPage.emailInput().clear()
        paymentRequestPage.emailInput().send_keys('adasdjrew%^^8942')
        log.info("Email input data - " + f"'{paymentRequestPage.emailInput().get_attribute('value')}'")

        log.info("Filling amount ")
        paymentRequestPage.amountInput().clear()
        paymentRequestPage.amountInput().send_keys('0cxvcx')
        log.info("Amount input data - " + f"'{paymentRequestPage.amountInput().get_attribute('value')}'")

        log.info("Submit form")
        paymentRequestPage.sendPaymentRequest().click()
        time.sleep(2)
        log.info("Email validation message " + f"'{paymentRequestPage.emailError().text}'")
        assert ('The email format is invalid' in paymentRequestPage.emailError().text)
        log.info("Email validation message " + f"'{paymentRequestPage.amountError().text}'")
        assert ('The amount must be at least' in paymentRequestPage.amountError().text)

    # Test create payment request with special characters
    def test_create_payment_request_with_special(self):
        """Test create payment request with special characters"""
        log = self.myLogger()
        paymentRequestPage = PaymentRequestPage(self.driver)

        log.info("Filling email ")
        paymentRequestPage.emailInput().clear()
        paymentRequestPage.emailInput().send_keys('--@*&$#(*)')
        log.info("Email input data - " + f"'{paymentRequestPage.emailInput().get_attribute('value')}'")

        log.info("Filling amount ")
        paymentRequestPage.amountInput().clear()
        paymentRequestPage.amountInput().send_keys('++')
        log.info("Amount input data - " + f"'{paymentRequestPage.amountInput().get_attribute('value')}'")

        log.info("Submit form")
        paymentRequestPage.sendPaymentRequest().click()
        time.sleep(2)
        log.info("Email validation message " + f"'{paymentRequestPage.emailError().text}'")
        assert ('The email format is invalid' in paymentRequestPage.emailError().text)
        log.info("Email validation message " + f"'{paymentRequestPage.amountError().text}'")
        assert ('The amount field is required' in paymentRequestPage.amountError().text)

    # Test create payment request with JS and PHP code
    def test_create_payment_request_with_js_php(self):
        """Test create payment request with JS and PHP code"""
        log = self.myLogger()
        paymentRequestPage = PaymentRequestPage(self.driver)

        log.info("Filling email ")
        paymentRequestPage.emailInput().clear()
        paymentRequestPage.emailInput().send_keys('<?php die();?>')
        log.info("Email input data - " + f"'{paymentRequestPage.emailInput().get_attribute('value')}'")

        log.info("Filling amount ")
        paymentRequestPage.amountInput().clear()
        paymentRequestPage.amountInput().send_keys('<script>alert()</script>')
        log.info("Amount input data - " + f"'{paymentRequestPage.amountInput().get_attribute('value')}'")

        log.info("Submit form")
        paymentRequestPage.sendPaymentRequest().click()
        time.sleep(2)
        log.info("Email validation message " + f"'{paymentRequestPage.emailError().text}'")
        assert ('The email format is invalid' in paymentRequestPage.emailError().text)
        log.info("Email validation message " + f"'{paymentRequestPage.amountError().text}'")
        assert ('The amount field is required' in paymentRequestPage.amountError().text)

    # Test create payment request with scheduled date
    def test_create_payment_request_with_scheduled_date(self):
        """Test create payment request with scheduled date"""
        log = self.myLogger()
        fake = Faker()
        paymentRequestPage = PaymentRequestPage(self.driver)

        log.info("Filling email ")
        paymentRequestPage.emailInput().clear()
        email = fake.email()
        paymentRequestPage.emailInput().send_keys(email)
        log.info("Email input data - " + f"'{paymentRequestPage.emailInput().get_attribute('value')}'")

        log.info("Filling amount ")
        paymentRequestPage.amountInput().clear()
        amount = fake.pyint()
        paymentRequestPage.amountInput().send_keys(amount)
        log.info("Amount input data - " + f"'{paymentRequestPage.amountInput().get_attribute('value')}'")

        log.info("Opening more settings")
        paymentRequestPage.moreSettingsLink().click()

        log.info("Opening scheduled date calendar")
        shchedule_obj = self.time_obj(10)
        day = int(shchedule_obj.strftime('%d'))
        hour = int(shchedule_obj.strftime('%H'))
        min = int(shchedule_obj.strftime('%M'))
        #log.info("Scheduled date and time " + f"'{shchedule_obj.strftime('%a, %B %d, %Y %I:%M %p')}'")
        log.info("Scheduled day, hour and min " + f"'{shchedule_obj.strftime('%d, %H:%M')}'")
        paymentRequestPage.scheduleDateInput().click()
        paymentRequestPage.scheduleDay(day).click()
        paymentRequestPage.scheduleHour(hour).click()
        paymentRequestPage.scheduleMin(min).click()

        paymentRequestPage.selectScheduleDateButton().click()
        log.info("Selected schedule date is - " + paymentRequestPage.scheduleDateInput().get_attribute('value'))

        log.info("Submit form using send link")
        paymentRequestPage.sendPaymentRequest().click()
        time.sleep(2)
        log.info("Success Message " + paymentRequestPage.sentLinkSuccessMessage().text)
        assert('Payment Link Successfully Sent!' in paymentRequestPage.sentLinkSuccessMessage().text)
        requestId = self.getRequestKey()
        paymentRequestPage.closeModalBtn().click()

        log.info("Searching request with id - " + requestId)
        assert (len(self.searchRequestById(requestId)) > 0)
        time.sleep(2)
        log.info("Created request found with id - " + requestId)

        log.info("Matching requested email - " + email)
        email_matched = paymentRequestPage.findEmail().text
        assert(email_matched == email)
        log.info("Requested email matched with - " + email_matched)

        currency = paymentRequestPage.selectCurrency().get_attribute('alt')
        log.info("Matching requested amount - " + currency+str(amount))
        amount_matched = paymentRequestPage.findAmount().text
        requested_amount = currency+str(amount);
        assert (requested_amount == amount_matched)
        log.info("Requested amount matched with - " + amount_matched)



    def getRequestKey(self):
        log = self.myLogger()
        try:
            paymentRequestPage = PaymentRequestPage(self.driver)
            request_link = paymentRequestPage.getPaymentRequestLink().get_attribute('value')
            log.info("Request url is - "+request_link)
            link_list = request_link.split("/")
            log.info("Request id is - " + link_list[-1])
            return link_list[-1]
        except Exception as e:
            log.info("Error in getting request url- " + e)

    def searchRequestById(self, request_id):
        log = self.myLogger()
        paymentRequestPage = PaymentRequestPage(self.driver)
        log.info("Entered request id in filter is  - " + request_id)
        paymentRequestPage.filterInput().send_keys(request_id)
        time.sleep(2)
        log.info("Finding request")
        return paymentRequestPage.findRequestRows()





    # Test create payment request with expiry date
    # Test create payment request with charge back protection
    # Test create payment request with long text in description and terms input
    # Test create payment request with send payment link
    # Test create payment request with create payment link
    # Test create payment request with charge now link
    # Test create payment request with schedule payment link
