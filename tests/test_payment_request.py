import time,  datetime

import pytest
from faker import Faker
from selenium.common.exceptions import NoSuchElementException, WebDriverException

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
        log.info("Scheduled day, hour and min " + f"'{shchedule_obj.strftime('%d, %H:%M')}'")
        paymentRequestPage.scheduleDateInput().click()
        time.sleep(2)
        paymentRequestPage.scheduleDay(day).click()
        paymentRequestPage.scheduleHour(hour).click()
        paymentRequestPage.scheduleMin(min).click()

        paymentRequestPage.selectScheduleDateButton().click()
        log.info("Selected schedule date is - " + paymentRequestPage.scheduleDateInput().get_attribute('value'))
        time.sleep(2)
        log.info("Submit form using send link")
        paymentRequestPage.sendPaymentRequest().click()
        time.sleep(2)
        log.info("Success Message " + paymentRequestPage.sentLinkSuccessMessage().text)
        assert('Payment Link Successfully Sent!' in paymentRequestPage.sentLinkSuccessMessage().text)
        requestId = self.getRequestKey()
        paymentRequestPage.closeModalBtn().click()

        time.sleep(2)
        log.info("Searching request with id - " + requestId)
        time.sleep(2)
        searched_data = self.searchRequestById(requestId)

        if len(searched_data) == 0:
            log.info("Request not found with request id - " + requestId)
            return
        log.info("All Data")
        self.logRequestData(searched_data)
        log.info("Matching requested email - " + searched_data['email'])
        assert(searched_data['email'] == email)
        log.info("Requested email matched with - " + searched_data['email'])
        currency = paymentRequestPage.selectCurrency().get_attribute('alt')
        log.info("Matching requested amount - " + currency+str(amount))
        amount_matched = searched_data['amount']
        requested_amount = currency+str(amount)
        assert (requested_amount == amount_matched)
        log.info("Requested amount matched with - " + amount_matched)

    # Test create payment request with expiry date
    def test_create_payment_request_with_expiry_date(self):
        """Test create payment request with expiry date"""
        log = self.myLogger()
        fake = Faker()
        paymentRequestPage = PaymentRequestPage(self.driver)

        paymentRequestPage.addPaymentRequestLink().click()

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
        # paymentRequestPage.moreSettingsLink().click()

        log.info("Opening scheduled date calendar")
        shchedule_obj = self.time_obj(10)
        day = int(shchedule_obj.strftime('%d'))
        hour = int(shchedule_obj.strftime('%H'))
        min = int(shchedule_obj.strftime('%M'))
        # log.info("Scheduled date and time " + f"'{shchedule_obj.strftime('%a, %B %d, %Y %I:%M %p')}'")
        log.info("Scheduled day, hour and min " + f"'{shchedule_obj.strftime('%d, %H:%M')}'")
        paymentRequestPage.scheduleDateInput().click()
        paymentRequestPage.scheduleDay(day).click()
        paymentRequestPage.scheduleHour(hour).click()
        paymentRequestPage.scheduleMin(min).click()
        log.info("Closing schedule date calendar")
        paymentRequestPage.selectScheduleDateButton().click()
        log.info("Selected schedule date is - " + paymentRequestPage.scheduleDateInput().get_attribute('value'))
        time.sleep(1)
        log.info("Opening expiry date calendar")
        exp_obj = self.time_obj(81)
        day = int(exp_obj.strftime('%d'))
        hour = int(exp_obj.strftime('%H'))
        min = int(exp_obj.strftime('%M'))
        log.info("Expiry day, hour and min " + f"'{exp_obj.strftime('%d, %H:%M')}'")
        log.info("Opening expiry calendar")
        paymentRequestPage.expiryDateInput().click()
        log.info("expiryDateInput")
        paymentRequestPage.expiryDay(day).click()
        paymentRequestPage.expiryHour(hour).click()
        paymentRequestPage.expiryMin(min).click()
        log.info("Closing expiry date calendar")
        paymentRequestPage.selectExpiryDateButton().click()
        log.info("Selected expiry date is - " + paymentRequestPage.expiryDateInput().get_attribute('value'))

        log.info("Submit form using send link")
        time.sleep(1)
        paymentRequestPage.sendPaymentRequest().click()
        time.sleep(2)
        log.info("Success Message " + paymentRequestPage.sentLinkSuccessMessage().text)
        assert ('Payment Link Successfully Sent!' in paymentRequestPage.sentLinkSuccessMessage().text)
        requestId = self.getRequestKey()
        paymentRequestPage.closeModalBtn().click()
        time.sleep(2)
        log.info("Searching request with id - " + requestId)
        searched_data = self.searchRequestById(requestId)

        if len(searched_data) == 0:
            log.info("Request not found with request id - " + requestId)
            return
        log.info("All Data")
        self.logRequestData(searched_data)

        log.info("Created request found with id - " + requestId)
        log.info("Matching requested email - " + email)
        email_matched = searched_data['email']
        assert (email_matched == email)
        log.info("Requested email matched with - " + email_matched)

        currency = paymentRequestPage.selectCurrency().get_attribute('alt')
        log.info("Matching requested amount - " + currency + str(amount))
        amount_matched = searched_data['amount']
        requested_amount = currency + str(amount)
        assert (requested_amount == amount_matched)
        log.info("Requested amount matched with - " + amount_matched)

    # Test creating payment request with wrong schedule date
    def test_create_payment_request_with_wrong_scheduled_date(self):
        """Test creating payment request with wrong schedule date"""
        log = self.myLogger()
        fake = Faker()
        paymentRequestPage = PaymentRequestPage(self.driver)
        paymentRequestPage.addPaymentRequestLink().click()

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
        #paymentRequestPage.moreSettingsLink().click()

        log.info("Opening scheduled date calendar")
        shchedule_obj = self.time_obj(0)
        day = int(shchedule_obj.strftime('%d'))
        hour = int(shchedule_obj.strftime('%H'))
        min = int(shchedule_obj.strftime('%M'))
        # log.info("Scheduled date and time " + f"'{shchedule_obj.strftime('%a, %B %d, %Y %I:%M %p')}'")
        log.info("Scheduled day, hour and min " + f"'{shchedule_obj.strftime('%d, %H:%M')}'")
        paymentRequestPage.scheduleDateInput().click()
        time.sleep(1)
        paymentRequestPage.scheduleDay(day).click()
        paymentRequestPage.scheduleHour(hour).click()
        paymentRequestPage.scheduleMin(min).click()

        paymentRequestPage.selectScheduleDateButton().click()
        log.info("Selected schedule date is - " + paymentRequestPage.scheduleDateInput().get_attribute('value'))
        time.sleep(2)
        log.info("Submit form using send link")
        paymentRequestPage.sendPaymentRequest().click()

        assert ('Due date must be a future date and time' in paymentRequestPage.scheduleDateError().text)
        log.info("Scheduled date error message - " + paymentRequestPage.scheduleDateError().text)
        paymentRequestPage.closeRequestModalButton().click()

    # Test create payment request with wrong expiry date
    def test_create_payment_request_with_wrong_expiry_date(self):
        """Test create payment request with wrong expiry date"""
        log = self.myLogger()
        fake = Faker()
        paymentRequestPage = PaymentRequestPage(self.driver)
        paymentRequestPage.addPaymentRequestLink().click()

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
        # paymentRequestPage.moreSettingsLink().click()
        # paymentRequestPage.scheduleDateInput().clear()
        log.info("Opening expiry date calendar")
        exp_obj = self.time_obj(0)
        day = int(exp_obj.strftime('%d'))
        hour = int(exp_obj.strftime('%H'))
        min = int(exp_obj.strftime('%M'))
        log.info("Expiry day, hour and min " + f"'{exp_obj.strftime('%d, %H:%M')}'")
        log.info("Opening expiry calendar")
        paymentRequestPage.expiryDateInput().click()
        log.info("expiryDateInput")
        paymentRequestPage.expiryDay(day).click()
        paymentRequestPage.expiryHour(hour).click()
        paymentRequestPage.expiryMin(min).click()
        log.info("Closing expiry date calendar")
        paymentRequestPage.selectExpiryDateButton().click()
        log.info("Selected expiry date is - " + paymentRequestPage.expiryDateInput().get_attribute('value'))

        log.info("Submit form using send link")
        paymentRequestPage.sendPaymentRequest().click()
        time.sleep(2)

        assert ('Expiry date must be a future date' in paymentRequestPage.expiryDateError().text)
        paymentRequestPage.closeRequestModalButton().click()

    # Test create payment request with charge back protection
    def test_create_payment_request_with_chargeback(self):
        """Test create payment request with charge back protection"""
        log = self.myLogger()
        fake = Faker()
        paymentRequestPage = PaymentRequestPage(self.driver)
        paymentRequestPage.addPaymentRequestLink().click()
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
        #paymentRequestPage.moreSettingsLink().click()

        log.info("Selecting charge back protection on")
        paymentRequestPage.onChargeBackButton().click()

        log.info("Submit form using send link")
        paymentRequestPage.sendPaymentRequest().click()
        time.sleep(2)
        log.info("Success Message " + paymentRequestPage.sentLinkSuccessMessage().text)
        assert ('Payment Link Successfully Sent!' in paymentRequestPage.sentLinkSuccessMessage().text)
        requestId = self.getRequestKey()
        paymentRequestPage.closeModalBtn().click()

        time.sleep(2)
        log.info("Searching request with id - " + requestId)

        searched_data = self.searchRequestById(requestId)
        if len(searched_data) == 0:
            log.info("Request not found with request id - " + requestId)
            return
        log.info("All Data")
        self.logRequestData(searched_data)

        log.info("Created request found with id - " + requestId)

        log.info("Matching requested email - " + email)
        email_matched = searched_data['email']
        assert (email_matched == email)
        log.info("Requested email matched with - " + email_matched)

        currency = paymentRequestPage.selectCurrency().get_attribute('alt')
        log.info("Matching requested amount - " + currency + str(amount))
        amount_matched = searched_data['amount']
        requested_amount = currency + str(amount)
        assert (requested_amount == amount_matched)
        log.info("Requested amount matched with - " + amount_matched)
        log.info("Charge back protection status " + searched_data['chargeback_protection_label'])
        assert(searched_data['chargeback_protection_label'] == 'Yes')

    # Test create payment request with long text in description and terms input
    def test_create_payment_request_with_long_desc_and_terms(self):
        """Test create payment request with long text in description and terms input"""
        log = self.myLogger()
        fake = Faker()
        paymentRequestPage = PaymentRequestPage(self.driver)
        paymentRequestPage.filterInput().clear()
        paymentRequestPage.addPaymentRequestLink().click()
        log.info("Filling email ")
        paymentRequestPage.emailInput().clear()
        email = fake.email()
        paymentRequestPage.emailInput().send_keys(email)
        log.info("Email input data - " + f"'{paymentRequestPage.emailInput().get_attribute('value')}'")

        log.info("Filling amount ")
        paymentRequestPage.amountInput().clear()
        amount = 25
        paymentRequestPage.amountInput().send_keys(amount)
        log.info("Amount input data - " + f"'{paymentRequestPage.amountInput().get_attribute('value')}'")

        dummy_text = ""
        for _ in range(5):
            dummy_text += fake.paragraph(nb_sentences=5)

        log.info("Filling description data")
        paymentRequestPage.descriptionInput().send_keys(dummy_text)
        log.info("Description text is - "+paymentRequestPage.descriptionInput().get_attribute('value'))

        log.info("Opening more settings")
        # paymentRequestPage.moreSettingsLink().click()

        log.info("Filling term data")
        paymentRequestPage.termsInput().send_keys(dummy_text)
        log.info("Terms text is - " + paymentRequestPage.termsInput().get_attribute('value'))

        log.info("Submit form using send link")
        paymentRequestPage.sendPaymentRequest().click()
        time.sleep(2)
        log.info("Success Message " + paymentRequestPage.sentLinkSuccessMessage().text)
        assert ('Payment Link Successfully Sent!' in paymentRequestPage.sentLinkSuccessMessage().text)
        requestId = self.getRequestKey()
        paymentRequestPage.closeModalBtn().click()

        time.sleep(2)
        log.info("Searching request with id - " + requestId)
        searched_data = self.searchRequestById(requestId)
        if len(searched_data) == 0:
            log.info("Request not found with request id - " + requestId)
            return
        log.info("All Data")
        self.logRequestData(searched_data)

        log.info("Matching requested email - " + email)
        email_matched = searched_data['email']
        assert (email_matched == email)
        log.info("Requested email matched with - " + email_matched)

        currency = paymentRequestPage.selectCurrency().get_attribute('alt')
        log.info("Matching requested amount - " + currency + str(amount))
        amount_matched = searched_data['amount']
        requested_amount = currency + str(amount)
        assert (requested_amount == amount_matched)
        log.info("Requested amount matched with - " + amount_matched)

        log.info("Matching description")
        assert(searched_data['description'] in dummy_text)
        log.info('Found the description is - ' + searched_data['description'])

        log.info("Matching terms")
        assert (searched_data['terms'] in dummy_text)
        log.info('Found the terms is - ' + searched_data['terms'])

    # Test create payment request with create payment link
    def test_payment_request_create_payment_link(self):
        """Test create payment request with create payment link"""
        log = self.myLogger()
        fake = Faker()
        paymentRequestPage = PaymentRequestPage(self.driver)
        paymentRequestPage.filterInput().clear()
        paymentRequestPage.addPaymentRequestLink().click()
        time.sleep(2)
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

        log.info("Opening expand menu link")
        paymentRequestPage.menuListButton().click()

        log.info("Submit form using create payment link")
        paymentRequestPage.createPaymentLink().click()
        time.sleep(2)
        log.info("Success Message " + paymentRequestPage.createLinkSuccessMessage().text)
        assert ('Payment link successfully created' in paymentRequestPage.createLinkSuccessMessage().text)
        requestId = self.getRequestKey()
        paymentRequestPage.closeSentLinkModalBtn().click()

        time.sleep(2)
        log.info("Searching request with id - " + requestId)
        searched_data = self.searchRequestById(requestId)
        if len(searched_data) == 0:
            log.info("Request not found with request id - " + requestId)
            return
        log.info("All Data")
        self.logRequestData(searched_data)

        log.info("Created request found with id - " + requestId)

        log.info("Matching requested email - " + email)
        email_matched = searched_data['email']
        assert (email_matched == email)
        log.info("Requested email matched with - " + email_matched)

        currency = paymentRequestPage.selectCurrency().get_attribute('alt')
        log.info("Matching requested amount - " + currency + str(amount))
        amount_matched = searched_data['amount']
        requested_amount = currency + str(amount)
        assert (requested_amount == amount_matched)
        log.info("Requested amount matched with - " + amount_matched)

    # Test create payment request with charge now payment link
    def test_payment_request_charge_now_link(self):
        """Test create payment request with charge now payment link"""
        log = self.myLogger()
        fake = Faker()
        paymentRequestPage = PaymentRequestPage(self.driver)
        paymentRequestPage.filterInput().clear()
        paymentRequestPage.addPaymentRequestLink().click()
        time.sleep(2)
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

        log.info("Opening expand menu link")
        paymentRequestPage.menuListButton().click()

        log.info("Submit form using charge now link")
        paymentRequestPage.chargePaymentLink().click()
        time.sleep(2)

        try:
            log.info("Clicking to add new credit card link")
            paymentRequestPage.addPaymentRequestLink().click()
        except WebDriverException:
            log.info("Add card link is not exists")
            pass
        name = fake.name()
        log.info("Adding Name on card " + name)
        paymentRequestPage.nameOnCard().send_keys(name)

        log.info("Adding card - 4242424242424242 12/25 123 55555")
        paymentRequestPage.addCard("4242424242424242122512355555")

        time.sleep(2)
        self.driver.switch_to.default_content()
        log.info("Charging now")
        paymentRequestPage.chargeNowBtn().click()
        time.sleep(2)

        successMessage = paymentRequestPage.paymentSuccessMessage().text;
        log.info("Success Message - " + successMessage)
        assert ('Payment successfully charged' in successMessage)

        requestId = self.getRequestKey()
        time.sleep(2)
        log.info("Searching request with id - " + requestId)

        searched_data = self.searchRequestById(requestId)
        if len(searched_data) == 0:
            log.info("Request not found with request id - " + requestId)
            return
        log.info("All Data")
        self.logRequestData(searched_data)

        log.info("Created request found with id - " + requestId)

        log.info("Matching requested email - " + email)
        email_matched = searched_data['email']
        assert (email_matched == email)
        log.info("Requested email matched with - " + email_matched)

        currency = paymentRequestPage.selectCurrency().get_attribute('alt')
        log.info("Matching requested amount - " + currency + str(amount))
        amount_matched = searched_data['amount']
        requested_amount = currency + str(amount)
        assert (requested_amount == amount_matched)
        log.info("Requested amount matched with - " + amount_matched)
        log.info("Payment status is " + searched_data['payment_status'])
        assert ('Paid' in searched_data['payment_status'])

    # Test create payment request with charge now payment link without adding card
    def test_payment_request_charge_now_link_without_card(self):
        """Test create payment request with charge now payment link without adding card"""
        log = self.myLogger()
        fake = Faker()
        paymentRequestPage = PaymentRequestPage(self.driver)
        paymentRequestPage.filterInput().clear()
        paymentRequestPage.addPaymentRequestLink().click()
        time.sleep(2)
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

        log.info("Opening expand menu link")
        paymentRequestPage.menuListButton().click()

        log.info("Submit form using charge now link")
        paymentRequestPage.chargePaymentLink().click()
        time.sleep(2)
        log.info("Charging now")
        paymentRequestPage.chargeNowBtn().click()

        fullname = paymentRequestPage.fullNameError().text;
        log.info("Error Message - " + fullname)
        assert ('Please enter name on card' in fullname)

    # Test create payment request with schedule payment link
    def test_payment_request_schedule_charge_link(self):
        """Test create payment request with schedule charge link"""
        log = self.myLogger()
        fake = Faker()
        paymentRequestPage = PaymentRequestPage(self.driver)
        paymentRequestPage.filterInput().clear()
        paymentRequestPage.addPaymentRequestLink().click()
        time.sleep(2)
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

        log.info("Opening expand menu link")
        paymentRequestPage.menuListButton().click()

        log.info("Submit form using schedule charge link")
        paymentRequestPage.scheduleChargeLink().click()
        time.sleep(2)

        scheduleDateError = paymentRequestPage.scheduleDateError().text
        log.info("Schedule Date error - "+scheduleDateError)
        assert('You need to select date and time to schedule payment' in scheduleDateError)

        log.info("Opening scheduled date calendar")
        shchedule_obj = self.time_obj(10)
        day = int(shchedule_obj.strftime('%d'))
        hour = int(shchedule_obj.strftime('%H'))
        min = int(shchedule_obj.strftime('%M'))
        # log.info("Scheduled date and time " + f"'{shchedule_obj.strftime('%a, %B %d, %Y %I:%M %p')}'")
        log.info("Scheduled day, hour and min " + f"'{shchedule_obj.strftime('%d, %H:%M')}'")
        paymentRequestPage.scheduleDateInput().click()
        time.sleep(1)
        paymentRequestPage.scheduleDay(day).click()
        paymentRequestPage.scheduleHour(hour).click()
        paymentRequestPage.scheduleMin(min).click()

        paymentRequestPage.selectScheduleDateButton().click()
        log.info("Selected schedule date is - " + paymentRequestPage.scheduleDateInput().get_attribute('value'))
        time.sleep(2)
        log.info("Submit form using send link")
        paymentRequestPage.sendPaymentRequest().click()
        time.sleep(2)
        log.info("Success Message " + paymentRequestPage.sentLinkSuccessMessage().text)
        assert ('Payment Link Successfully Sent!' in paymentRequestPage.sentLinkSuccessMessage().text)
        requestId = self.getRequestKey()
        paymentRequestPage.closeModalBtn().click()

        time.sleep(2)
        log.info("Searching request with id - " + requestId)
        assert (len(self.searchRequestById(requestId)) > 0)

        log.info("Created request found with id - " + requestId)

        log.info("Matching requested email - " + email)
        email_matched = paymentRequestPage.findEmail().text
        assert (email_matched == email)
        log.info("Requested email matched with - " + email_matched)

        currency = paymentRequestPage.selectCurrency().get_attribute('alt')
        log.info("Matching requested amount - " + currency + str(amount))
        amount_matched = paymentRequestPage.findAmount().text
        requested_amount = currency + str(amount)
        assert (requested_amount == amount_matched)
        log.info("Requested amount matched with - " + amount_matched)

    def getRequestKey(self):
        log = self.myLogger()
        try:
            paymentRequestPage = PaymentRequestPage(self.driver)
            request_link = paymentRequestPage.getPaymentRequestLink().get_attribute('value')
            log.info("Request url is - " + request_link)
            link_list = request_link.split("/")
            log.info("Request id is - " + link_list[-1])
            return link_list[-1]
        except Exception as e:
            log.info("Error in getting request url- " + e)

    def searchRequestById(self, request_id):
        log = self.myLogger()
        paymentRequestPage = PaymentRequestPage(self.driver)
        log.info("Entered request id in filter is  - " + request_id)
        paymentRequestPage.filterInput().clear()
        paymentRequestPage.filterInput().send_keys(request_id)
        time.sleep(2)
        log.info("Finding request")
        assert(len(paymentRequestPage.findRequestRows())>0)
        paymentRequestPage.toggleRowButton().click()
        if len(paymentRequestPage.findRequestRows()) > 0:
            request_type = paymentRequestPage.findRequestType().get_attribute('title')
            amount = paymentRequestPage.findAmount().text
            request_id = paymentRequestPage.findRequestIdLabel().text
            payment_status = paymentRequestPage.paymentStatusLabel().text if paymentRequestPage.paymentStatusLabel() else ""
            email = paymentRequestPage.findEmail().text if paymentRequestPage.findEmail() else ""

            paid_on = paymentRequestPage.findPaidOnDate().text if paymentRequestPage.findPaidOnDate() else ""
            scheduled_date_label = paymentRequestPage.findScheduleDateLabel().text if paymentRequestPage.findScheduleDateLabel() else ""
            expiry_date_label = paymentRequestPage.findExpiryDateLabel().text if paymentRequestPage.findExpiryDateLabel() else ""
            chargeback_protection_label = paymentRequestPage.findChargebackProtectionLabel().text if paymentRequestPage.findChargebackProtectionLabel() else ""
            payment_method = paymentRequestPage.findPaymentMethodLabel().text if paymentRequestPage.findPaymentMethodLabel() else ""
            description = paymentRequestPage.findDescription().text if paymentRequestPage.findDescription() else ""
            terms = paymentRequestPage.findTerms().text if paymentRequestPage.findTerms() else ""
            txn_ref = paymentRequestPage.findRequestIdLabel().text if paymentRequestPage.findReferenceNumber() else ""

            return {
                    'request_type': request_type, 'amount': amount, 'request_id': request_id, 'payment_status': payment_status, 'email': email, 'paid_on': paid_on,
                    'scheduled_date_label': scheduled_date_label, 'expiry_date_label': expiry_date_label, 'chargeback_protection_label': chargeback_protection_label, 'payment_method': payment_method,
                    'description': description, 'terms': terms, 'txn_ref': txn_ref,
                    }


    def logRequestData(self, logData):
        log = self.myLogger()
        log.info("Request type: " + logData['request_type'])
        log.info("Request Amount: " + logData['amount'])
        log.info("Request ID: " + logData['request_id'])
        log.info("Payment Status: " + logData['payment_status'])
        log.info("Email: " + logData['email'])
        log.info("Paid On: " + logData['paid_on'])
        log.info("Schedule date: " + logData['scheduled_date_label'])
        log.info("Expiry date: " + logData['expiry_date_label'])
        log.info("Chargeback Protection: " + logData['chargeback_protection_label'])
        log.info("Payment method: " + logData['payment_method'])
        log.info("Description: " + logData['description'])
        log.info("Terms: " + logData['terms'])
        log.info("Txn ref: " + logData['txn_ref'])


