import time

from pages.HomePage import HomePage
from pages.SignupPage import SignupPage
from utilities.BaseClass import BaseClass


class TestSignup(BaseClass):

    def test_signup_link(self):
        """Opening home page and clicking to signup link"""
        homePage = HomePage(self.driver)
        log = self.myLogger()
        log.info("Clicking to signup button")
        homePage.signupBtn().click()

    def test_signup_with_blank_data(self):
        """Test signup with blank data"""
        log = self.myLogger()
        signup = SignupPage(self.driver)
        log.info("Input data in full name field")
        signup.fullName().send_keys("")
        log.info("Full Name - " + f"'{signup.fullName().get_attribute('value')}'")
        signup.companyName().send_keys("")
        log.info("Company Name - " + f"'{signup.companyName().get_attribute('value')}'")
        signup.phone().send_keys("")
        log.info("Phone no - " + f"'{signup.phone().get_attribute('value')}'")
        signup.email().send_keys("")
        log.info("Email - " + f"'{signup.email().get_attribute('value')}'")
        signup.password().send_keys("")
        log.info("Password - " + f"'{signup.password().get_attribute('value')}'")
        signup.confirm_password().send_keys("")
        log.info("Confirm Password - " + f"'{signup.confirm_password().get_attribute('value')}'")
        signup.pms().send_keys("")
        log.info("PMS - " + f"'{signup.pms().get_attribute('value')}'")
        signup.agree().click()
        log.info("PMS - Terms accepted")
        log.info('Submitting signup form')
        signup.signupSubmit().click()
        time.sleep(2)

        log.info('Full name error message: ' + signup.fullNameError().text)
        assert ('full name' in signup.fullNameError().text)

        log.info('Company name error message: ' + signup.companyNameError().text)
        assert ('company name' in signup.companyNameError().text)

        log.info('Phone error message: ' + signup.phoneError().text)
        assert ('phone number' in signup.phoneError().text)

        log.info('Email error message: ' + signup.emailError().text)
        assert ('email address' in signup.emailError().text)




    # Test sign up with invalid email

    # Test sign up with min length password

    # Test signup with not matching password

    # Test signup with existing email

    # Test signup without accepting terms

    # Test signup with valid email






