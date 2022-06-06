import time

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from faker import Faker


class TestLogin(BaseClass):


    # testing login with blank email and password
    def test_login_without_data(self):
        """Test login with blank form data"""
        home_page = HomePage(self.driver)
        log = self.myLogger()
        log.info('testing login with blank email and password')
        log.info('Login button clicked')
        home_page.loginBtn().click()

        login_page = LoginPage(self.driver)
        login_page.emailInput().send_keys('')
        log.info('email id: ')
        login_page.passwordInput().send_keys('')
        log.info('password: ')
        login_page.loginSubmitBtn().click()
        time.sleep(2)
        log.info('Email error message: ' + login_page.emailError().text)
        assert(login_page.emailError().text in 'Email is required')
        log.info('Password error message: ' + login_page.passwordError().text)
        assert(login_page.passwordError().text in 'Password is required')

    # test with invalid email and blank password
    def test_login_with_invalid_email_blank_password(self):
        """Test with invalid email and blank password"""
        #self.driver.refresh()
        log = self.myLogger()
        log.info('test with invalid email and blank password')
        login_page = LoginPage(self.driver)
        login_page.emailInput().send_keys('invalid_email')
        log.info('email id: ' + login_page.emailInput().get_attribute('value'))
        login_page.passwordInput().clear()
        log.info('password: ' + login_page.passwordInput().get_attribute('value'))
        login_page.loginSubmitBtn().click()
        time.sleep(2)
        log.info('Email error message: ' + login_page.emailError().text)
        assert(login_page.emailError().text in 'The email must be a valid email address.')
        log.info('Password error message: ' + login_page.passwordError().text)
        assert(login_page.passwordError().text in 'Password is required')

    # testing login with invalid email
    def test_login_with_invalid_email(self):
        """ Test with invalid email and valid password """
        # self.driver.refresh()
        log = self.myLogger()
        log.info('testing login with invalid email')
        login_page = LoginPage(self.driver)
        log.info('Passed email: invalid_email')
        login_page.emailInput().clear()
        login_page.emailInput().send_keys('invalid_email')
        login_page.passwordInput().send_keys('123456')
        log.info('password: 123456')
        login_page.loginSubmitBtn().click()
        time.sleep(3)
        login_page.passwordInput().clear()
        log.info('Email error message: ' + login_page.emailError().text)
        assert (login_page.emailError().text in 'The email must be a valid email address.')

    # test with valid email and blank password
    def test_login_with_valid_email_blank_password(self):
        """ Test with valid email and blank password """
        self.driver.refresh()
        log = self.myLogger()
        log.info('test with valid email and blank password')
        login_page = LoginPage(self.driver)
        login_page.emailInput().clear()
        login_page.emailInput().send_keys('rajan@yopmail.com')
        log.info('email id: ' + login_page.emailInput().get_attribute('value'))
        login_page.passwordInput().clear()
        login_page.passwordInput().send_keys('')
        log.info('password: ' + login_page.passwordInput().get_attribute('value'))
        login_page.loginSubmitBtn().click()
        time.sleep(3)
        log.info('Password error message: ' + login_page.passwordError().text)
        assert (login_page.passwordError().text in 'Password is required')

    # test Login with js and php code
    def test_login_with_js_code(self):
        """ Test with JS code in email and password """
        log = self.myLogger()
        log.info('test Login with js code')
        login_page = LoginPage(self.driver)
        login_page.emailInput().clear()
        login_page.emailInput().send_keys('<script>alert("hello")</script>')
        log.info('email id: ' + login_page.emailInput().get_attribute('value'))
        login_page.passwordInput().clear()
        login_page.passwordInput().send_keys('<script>alert("hello")</script>')
        log.info('password: ' + login_page.passwordInput().get_attribute('value'))
        login_page.loginSubmitBtn().click()
        time.sleep(3)
        log.info('Email error message: ' + login_page.emailError().text)
        assert (login_page.emailError().text in 'The email must be a valid email address.')

    # test Login with js code
    def test_login_with_php_code(self):
        """ Test with PHP code in email and password """
        log = self.myLogger()
        log.info('test Login with php code')
        login_page = LoginPage(self.driver)
        login_page.emailInput().clear()
        login_page.emailInput().send_keys('<?php die() ?>')
        log.info('email id: ' + login_page.emailInput().get_attribute('value'))
        login_page.passwordInput().clear()
        login_page.passwordInput().send_keys('<?php die() ?>')
        log.info('password: ' + login_page.passwordInput().get_attribute('value'))
        login_page.loginSubmitBtn().click()
        time.sleep(3)
        log.info('Email error message: ' + login_page.emailError().text)
        assert (login_page.emailError().text in 'The email must be a valid email address.')

    # test Login with long password
    def test_login_with_long_password(self):
        """ Test with long password """
        fake = Faker()
        log = self.myLogger()
        log.info('test Login with long password')
        login_page = LoginPage(self.driver)
        login_page.emailInput().clear()
        login_page.emailInput().send_keys('rajan@yopmail.com')
        log.info('email id: ' + login_page.emailInput().get_attribute('value'))
        login_page.passwordInput().clear()
        login_page.passwordInput().send_keys(fake.sentence()+fake.sentence()+fake.sentence()+fake.sentence())
        log.info('password: ' + login_page.passwordInput().get_attribute('value'))
        login_page.loginSubmitBtn().click()
        time.sleep(3)
        log.info('Email error message: ' + login_page.emailError().text)
        assert (login_page.emailError().text in 'These credentials do not match our records.')

    # testing login with special characters in email
    def test_login_with_special_characters_in_email(self):
        """ Test with special characters in email """
        # self.driver.refresh()
        log = self.myLogger()
        log.info('testing login with special characters in email')
        login_page = LoginPage(self.driver)
        login_page.emailInput().clear()
        login_page.emailInput().send_keys('-- @ !&*%$#)(+_')
        log.info('email id: ' + login_page.emailInput().get_attribute('value'))
        login_page.passwordInput().send_keys('123456')
        log.info('password: 123456')
        login_page.loginSubmitBtn().click()
        time.sleep(3)
        login_page.passwordInput().clear()
        log.info('Email error message: ' + login_page.emailError().text)
        assert (login_page.emailError().text in 'The email must be a valid email address.')

    # test with nonexistent email and password
    def test_login_with_valid_nonexists_email_and_password(self):
        """ Test with non-existing email and valid password """
        #self.driver.refresh()
        log = self.myLogger()
        fake = Faker()
        log.info('test with nonexistent email and password')
        login_page = LoginPage(self.driver)
        login_page.emailInput().clear()
        login_page.emailInput().send_keys(fake.email())
        log.info('email id: ' + login_page.emailInput().get_attribute('value'))
        login_page.passwordInput().clear()
        login_page.passwordInput().send_keys("123456")
        log.info('password: ' + login_page.passwordInput().get_attribute('value'))
        login_page.loginSubmitBtn().click()
        time.sleep(3)
        log.info('Email error message: ' + login_page.emailError().text)
        assert (login_page.emailError().text in 'These credentials do not match our records.')

 # test with nonexistent email and password
    def test_login_with_valid_email_and_password(self):
        """ Test with valid email and valid password """
        #self.driver.refresh()
        log = self.myLogger()
        log.info('test with valid email and password')
        login_page = LoginPage(self.driver)
        login_page.emailInput().clear()
        login_page.emailInput().send_keys('pgtest@yopmail.com')
        log.info('email id: ' + login_page.emailInput().get_attribute('value'))
        login_page.passwordInput().clear()
        login_page.passwordInput().send_keys("Rajan@123")
        log.info('password: ' + login_page.passwordInput().get_attribute('value'))
        login_page.loginSubmitBtn().click()
        time.sleep(4)
        log.info('Searching Dashboard Link: ')
        assert (login_page.dashbordLink())

