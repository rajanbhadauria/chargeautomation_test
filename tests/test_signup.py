import time

from faker import Faker

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
        log.info("Filling Form Data -- ")
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
        # signup.agree().click()
        log.info("Terms not accepted")
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

        log.info('Password error message: ' + signup.passwordError().text)
        assert ('Enter password' in signup.passwordError().text)

        log.info('Confirm password error message: ' + signup.confirmPasswordError().text)
        assert ('confirm password' in signup.confirmPasswordError().text)

        log.info('Terms error message: ' + signup.agreeError().text)
        assert ('terms and conditions' in signup.agreeError().text)

    # Test signup with invalid email
    def test_signup_with_invalid_email(self):
        """Test signup with invalid email"""
        log = self.myLogger()
        signup = SignupPage(self.driver)
        fake = Faker()
        log.info("Filling Form Data -- ")
        signup.fullName().send_keys(fake.name())
        log.info("Full Name - " + f"'{signup.fullName().get_attribute('value')}'")
        signup.companyName().send_keys(fake.company())
        log.info("Company Name - " + f"'{signup.companyName().get_attribute('value')}'")
        signup.phone().send_keys(fake.phone_number())
        log.info("Phone no - " + f"'{signup.phone().get_attribute('value')}'")
        signup.email().send_keys(fake.user_name())
        log.info("Email - " + f"'{signup.email().get_attribute('value')}'")
        password = fake.password()
        signup.password().send_keys(password)
        log.info("Password - " + f"'{signup.password().get_attribute('value')}'")
        signup.confirm_password().send_keys(password)
        log.info("Confirm Password - " + f"'{signup.confirm_password().get_attribute('value')}'")
        signup.pms().send_keys(fake.company())
        log.info("PMS - " + f"'{signup.pms().get_attribute('value')}'")
        signup.agree().click()
        log.info("Terms accepted")
        log.info('Submitting signup form')
        signup.signupSubmit().click()
        time.sleep(2)

        log.info('Email error message: ' + signup.emailError().text)
        assert ('valid email address' in signup.emailError().text)

    # Test signup with min length password
    def test_signup_with_min_lengh_password(self):
        """Test signup with min length password"""
        log = self.myLogger()
        signup = SignupPage(self.driver)
        fake = Faker()
        log.info("Filling Form Data -- ")
        signup.fullName().clear()
        signup.fullName().send_keys(fake.name())
        log.info("Full Name - " + f"'{signup.fullName().get_attribute('value')}'")
        signup.companyName().clear()
        signup.companyName().send_keys(fake.company())
        log.info("Company Name - " + f"'{signup.companyName().get_attribute('value')}'")
        signup.phone().clear()
        signup.phone().send_keys(fake.phone_number())
        log.info("Phone no - " + f"'{signup.phone().get_attribute('value')}'")
        signup.email().clear()
        signup.email().send_keys(fake.email())
        log.info("Email - " + f"'{signup.email().get_attribute('value')}'")
        password = "1"  # fake.password()
        signup.password().clear()
        signup.password().send_keys(password)
        log.info("Password - " + f"'{signup.password().get_attribute('value')}'")
        signup.confirm_password().clear()
        signup.confirm_password().send_keys(password)
        log.info("Confirm Password - " + f"'{signup.confirm_password().get_attribute('value')}'")
        signup.pms().clear()
        signup.pms().send_keys(fake.company())
        log.info("PMS - " + f"'{signup.pms().get_attribute('value')}'")
        signup.agree().click()
        log.info("Terms accepted")
        log.info('Submitting signup form')
        signup.signupSubmit().click()
        time.sleep(2)

        log.info('Password error message: ' + signup.passwordError().text)
        assert ('at least 6 characters' in signup.passwordError().text)

    # Test signup with not matching password and confirm password
    def test_signup_with_not_matching_password(self):
        """Test signup with not matching password and confirm password"""
        log = self.myLogger()
        signup = SignupPage(self.driver)
        fake = Faker()
        log.info("Filling Form Data -- ")
        signup.fullName().clear()
        signup.fullName().send_keys(fake.name())
        log.info("Full Name - " + f"'{signup.fullName().get_attribute('value')}'")
        signup.companyName().clear()
        signup.companyName().send_keys(fake.company())
        log.info("Company Name - " + f"'{signup.companyName().get_attribute('value')}'")
        signup.phone().clear()
        signup.phone().send_keys(fake.phone_number())
        log.info("Phone no - " + f"'{signup.phone().get_attribute('value')}'")
        signup.email().clear()
        signup.email().send_keys(fake.email())
        log.info("Email - " + f"'{signup.email().get_attribute('value')}'")
        signup.password().clear()
        signup.password().send_keys(fake.password())
        log.info("Password - " + f"'{signup.password().get_attribute('value')}'")
        signup.confirm_password().clear()
        signup.confirm_password().send_keys(fake.password())
        log.info("Confirm Password - " + f"'{signup.confirm_password().get_attribute('value')}'")
        signup.pms().clear()
        signup.pms().send_keys(fake.company())
        log.info("PMS - " + f"'{signup.pms().get_attribute('value')}'")
        signup.agree().click()
        log.info("Terms accepted")
        log.info('Submitting signup form')
        signup.signupSubmit().click()
        time.sleep(2)

        log.info('Password error message: ' + signup.passwordError().text)
        assert ('Password confirmation does not match' in signup.passwordError().text)

    # Test signup with existing email
    def test_signup_with_existing_email(self):
        """Test signup with existing email"""
        log = self.myLogger()
        signup = SignupPage(self.driver)
        fake = Faker()
        log.info("Filling Form Data -- ")
        signup.fullName().clear()
        signup.fullName().send_keys(fake.name())
        log.info("Full Name - " + f"'{signup.fullName().get_attribute('value')}'")

        signup.companyName().clear()
        signup.companyName().send_keys(fake.company())
        log.info("Company Name - " + f"'{signup.companyName().get_attribute('value')}'")

        signup.phone().clear()
        signup.phone().send_keys(fake.phone_number())
        log.info("Phone no - " + f"'{signup.phone().get_attribute('value')}'")

        signup.email().clear()
        signup.email().send_keys('pgtest@yopmail.com')
        log.info("Email - " + f"'{signup.email().get_attribute('value')}'")
        password = fake.password()

        signup.password().clear()
        signup.password().send_keys(password)
        log.info("Password - " + f"'{signup.password().get_attribute('value')}'")

        signup.confirm_password().clear()
        signup.confirm_password().send_keys(password)
        log.info("Confirm Password - " + f"'{signup.confirm_password().get_attribute('value')}'")

        signup.pms().clear()
        signup.pms().send_keys(fake.company())
        log.info("PMS - " + f"'{signup.pms().get_attribute('value')}'")

        signup.agree().click()
        log.info("Terms accepted")
        log.info('Submitting signup form')
        signup.signupSubmit().click()
        time.sleep(2)

        log.info('Email error message: ' + signup.emailError().text)
        assert ('Email address already exists' in signup.emailError().text)

    # Test signup without accepting terms
    def test_signup_without_accepting_terms(self):
        """Test signup without accepting terms"""
        log = self.myLogger()
        signup = SignupPage(self.driver)
        fake = Faker()
        log.info("Filling Form Data -- ")
        signup.fullName().clear()
        signup.fullName().send_keys(fake.name())
        log.info("Full Name - " + f"'{signup.fullName().get_attribute('value')}'")

        signup.companyName().clear()
        signup.companyName().send_keys(fake.company())
        log.info("Company Name - " + f"'{signup.companyName().get_attribute('value')}'")

        signup.phone().clear()
        signup.phone().send_keys(fake.phone_number())
        log.info("Phone no - " + f"'{signup.phone().get_attribute('value')}'")

        signup.email().clear()
        signup.email().send_keys(fake.email(domain='yopmail.com'))
        log.info("Email - " + f"'{signup.email().get_attribute('value')}'")
        password = fake.password()

        signup.password().clear()
        signup.password().send_keys(password)
        log.info("Password - " + f"'{signup.password().get_attribute('value')}'")

        signup.confirm_password().clear()
        signup.confirm_password().send_keys(password)
        log.info("Confirm Password - " + f"'{signup.confirm_password().get_attribute('value')}'")

        signup.pms().clear()
        signup.pms().send_keys(fake.company())
        log.info("PMS - " + f"'{signup.pms().get_attribute('value')}'")

        # signup.agree().click()
        log.info("Terms not accepted")
        log.info('Submitting signup form')
        signup.signupSubmit().click()
        time.sleep(2)

        log.info('Terms error message: ' + signup.agreeError().text)
        assert ('Please accept terms' in signup.agreeError().text)

    # Test signup with invalid phone number
    def test_signup_with_invalid_phone(self):
        """Test signup with invalid phone number"""
        log = self.myLogger()
        signup = SignupPage(self.driver)
        fake = Faker()
        log.info("Filling Form Data -- ")
        signup.fullName().clear()
        signup.fullName().send_keys(fake.name())
        log.info("Full Name - " + f"'{signup.fullName().get_attribute('value')}'")

        signup.companyName().clear()
        signup.companyName().send_keys(fake.company())
        log.info("Company Name - " + f"'{signup.companyName().get_attribute('value')}'")

        signup.phone().clear()
        signup.phone().send_keys('58585335034558945409504543534904')
        log.info("Phone no - " + f"'{signup.phone().get_attribute('value')}'")

        signup.email().clear()
        signup.email().send_keys(fake.email(domain='yopmail.com'))
        log.info("Email - " + f"'{signup.email().get_attribute('value')}'")
        password = fake.password()

        signup.password().clear()
        signup.password().send_keys(password)
        log.info("Password - " + f"'{signup.password().get_attribute('value')}'")

        signup.confirm_password().clear()
        signup.confirm_password().send_keys(password)
        log.info("Confirm Password - " + f"'{signup.confirm_password().get_attribute('value')}'")

        signup.pms().clear()
        signup.pms().send_keys(fake.company())
        log.info("PMS - " + f"'{signup.pms().get_attribute('value')}'")

        # signup.agree().click()
        log.info("Terms not accepted")
        log.info('Submitting signup form')
        signup.signupSubmit().click()
        time.sleep(2)

        log.info('Phone error message: ' + signup.phoneError().text)
        assert ('The phone may not be greater than 25' in signup.phoneError().text)

    # Test signup with special characters
    def test_signup_with_special_chars(self):
        """Test signup with special characters"""
        log = self.myLogger()
        signup = SignupPage(self.driver)
        fake = Faker()
        log.info("Filling Form Data -- ")
        signup.fullName().clear()
        signup.fullName().send_keys('--@$%*()_+|,":{]{}?></.,\-=')
        log.info("Full Name - " + f"'{signup.fullName().get_attribute('value')}'")

        signup.companyName().clear()
        signup.companyName().send_keys('--@$%*()_+|,":{]{}?></.,\-=')
        log.info("Company Name - " + f"'{signup.companyName().get_attribute('value')}'")

        signup.phone().clear()
        signup.phone().send_keys('--@$%*()_+|,":{]}')
        log.info("Phone no - " + f"'{signup.phone().get_attribute('value')}'")

        signup.email().clear()
        signup.email().send_keys('--@$%*()_+|,":{]{}?></.,\-=')
        log.info("Email - " + f"'{signup.email().get_attribute('value')}'")
        password = '--@$%*()_+|,":{]{}?></.,\-='

        signup.password().clear()
        signup.password().send_keys(password)
        log.info("Password - " + f"'{signup.password().get_attribute('value')}'")

        signup.confirm_password().clear()
        signup.confirm_password().send_keys(password)
        log.info("Confirm Password - " + f"'{signup.confirm_password().get_attribute('value')}'")

        signup.pms().clear()
        signup.pms().send_keys('--@$%*()_+|,":{]{}?></.,\-=')
        log.info("PMS - " + f"'{signup.pms().get_attribute('value')}'")

        # signup.agree().click()
        log.info("Terms not accepted")
        log.info('Submitting signup form')
        signup.signupSubmit().click()
        time.sleep(2)

        log.info('Full name error message: ' + signup.fullNameError().text)
        assert ('format is invalid.' in signup.fullNameError().text)

        log.info('Company name error message: ' + signup.companyNameError().text)
        assert ('Only alpha-numeric characters' in signup.companyNameError().text)

        # log.info('Phone error message: ' + signup.phoneError().text)
        # assert ('phone number' in signup.phoneError().text)

        log.info('Email error message: ' + signup.emailError().text)
        assert ('a valid email address' in signup.emailError().text)

        log.info('PMS error message: ' + signup.pmsError().text)
        assert ('current pms format' in signup.pmsError().text)

    # Test signup with js and php code
    def test_signup_with_js_php_code(self):
        """Test signup with js and php code"""
        log = self.myLogger()
        signup = SignupPage(self.driver)
        fake = Faker()
        log.info("Filling Form Data -- ")
        signup.fullName().clear()
        signup.fullName().send_keys('<script>alert("")</script>')
        log.info("Full Name - " + f"'{signup.fullName().get_attribute('value')}'")

        signup.companyName().clear()
        signup.companyName().send_keys('<script>alert("")</script>')
        log.info("Company Name - " + f"'{signup.companyName().get_attribute('value')}'")

        signup.phone().clear()
        signup.phone().send_keys('<?php echo "123"?>')
        log.info("Phone no - " + f"'{signup.phone().get_attribute('value')}'")

        signup.email().clear()
        signup.email().send_keys('<script>alert("")</script>')
        log.info("Email - " + f"'{signup.email().get_attribute('value')}'")
        password = '<script>alert("")</script><?php die();?>'

        signup.password().clear()
        signup.password().send_keys(password)
        log.info("Password - " + f"'{signup.password().get_attribute('value')}'")

        signup.confirm_password().clear()
        signup.confirm_password().send_keys(password)
        log.info("Confirm Password - " + f"'{signup.confirm_password().get_attribute('value')}'")

        signup.pms().clear()
        signup.pms().send_keys('<?php die();?>')
        log.info("PMS - " + f"'{signup.pms().get_attribute('value')}'")

        # signup.agree().click()
        log.info("Terms not accepted")
        log.info('Submitting signup form')
        signup.signupSubmit().click()
        time.sleep(2)

        log.info('Full name error message: ' + signup.fullNameError().text)
        assert ('format is invalid.' in signup.fullNameError().text)

        log.info('Company name error message: ' + signup.companyNameError().text)
        assert ('Only alpha-numeric characters' in signup.companyNameError().text)

        # log.info('Phone error message: ' + signup.phoneError().text)
        # assert ('phone number' in signup.phoneError().text)

        log.info('Email error message: ' + signup.emailError().text)
        assert ('a valid email address' in signup.emailError().text)

        log.info('PMS error message: ' + signup.pmsError().text)
        assert ('current pms format' in signup.pmsError().text)

    # Test signup with valid data
    def test_signup_with_valid_data(self):
        """Test signup with valid data"""
        log = self.myLogger()
        signup = SignupPage(self.driver)
        fake = Faker()
        log.info("Filling Form Data -- ")
        signup.fullName().clear()
        fullName = fake.name();
        signup.fullName().send_keys(fullName)
        log.info("Full Name - " + f"'{signup.fullName().get_attribute('value')}'")

        signup.companyName().clear()
        signup.companyName().send_keys(fake.last_name())
        log.info("Company Name - " + f"'{signup.companyName().get_attribute('value')}'")

        signup.phone().clear()
        signup.phone().send_keys(fake.phone_number())
        log.info("Phone no - " + f"'{signup.phone().get_attribute('value')}'")

        signup.email().clear()
        email = fake.email(domain='yopmail.com')
        signup.email().send_keys(email)
        log.info("Email - " + f"'{signup.email().get_attribute('value')}'")
        password = fake.password()

        signup.password().clear()
        signup.password().send_keys(password)
        log.info("Password - " + f"'{signup.password().get_attribute('value')}'")

        signup.confirm_password().clear()
        signup.confirm_password().send_keys(password)
        log.info("Confirm Password - " + f"'{signup.confirm_password().get_attribute('value')}'")

        signup.pms().clear()
        signup.pms().send_keys(fake.first_name())
        log.info("PMS - " + f"'{signup.pms().get_attribute('value')}'")

        signup.agree().click()
        log.info("Terms accepted")
        log.info('Submitting signup form')
        signup.signupSubmit().click()
        time.sleep(5)

        log.info('Success user name - ' + f"'{signup.signup_success_name().text}'")
        assert (fullName in signup.signup_success_name().text)

        log.info('Success user email - ' + f"'{signup.signup_success_message().text}'")
        assert (email in signup.signup_success_message().text)
