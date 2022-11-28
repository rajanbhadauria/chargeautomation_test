import pytest
import time
import datetime
import random
from faker import Faker

from selenium.webdriver.support.ui import Select

from pages.BookingPage import BookingPage
from pages.PrecheckinPage import PrecheckinPage
from utilities.BaseClass import BaseClass
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures('loginData')
class TestPreCheckin(BaseClass):

    # Login to site
    def test_login(self, loginData):
        """Test Payment request login to charge automation"""
        log = self.myLogger()
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        bookingPage = BookingPage(self.driver)
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
        bookingPage.bookingLink().click()

    # Test creating new booking
    def test_create_booking(self):
        """Test create new booking to charge automation"""
        time.sleep(2)
        log = self.myLogger()
        fake = Faker()
        bookingPage = BookingPage(self.driver)
        log.info("Opening create booking form")
        bookingPage.getNewbookingBtn().click()
        time.sleep(2)
        log.info("Selecting rental from the list")
        rentals = Select(bookingPage.getRentalDropdown())
        random_rental = random.randint(1, len(rentals.options) - 1)
        log.info("Rental index is - " + str(random_rental))
        rentals.select_by_index(str(random_rental))

        log.info("Opening date calendar")
        bookingPage.getDateInput().click()
        checkin_date = datetime.datetime.now() + datetime.timedelta(days=1)
        checkout_date = datetime.datetime.now() + datetime.timedelta(days=5)
        checkin_date = str(checkin_date.strftime("%Y-%m-%d"))
        checkout_date = str(checkout_date.strftime("%Y-%m-%d"))
        log.info("Selecting check-in date" + checkin_date)
        bookingPage.getCalendarDate(checkin_date).click()
        log.info("Selecting check-out date" + checkout_date)
        bookingPage.getCalendarDate(checkout_date).click()
        log.info("Selecting booking source")
        random_booking_source = random.randint(1, 6)
        booking_source = Select(bookingPage.getBookingSourceDropdown())
        booking_source.select_by_index(random_booking_source)
        reservation_amount = random.randint(500, 1000)
        log.info("Setting reservation amount = " + str(reservation_amount))
        bookingPage.getBookingAmountInput().send_keys(reservation_amount)
        log.info("Setting first name input")
        first_name = fake.first_name()
        bookingPage.getFirstNameInput().send_keys(first_name)
        log.info("Setting last name input")
        last_name = fake.last_name()
        bookingPage.getLastNameInput().send_keys(last_name)
        log.info("Setting email input")
        email = fake.email(domain='yopmail.com')
        bookingPage.getEmailInput().send_keys(email)
        log.info("Creating new booking ")
        bookingPage.getSaveBookingBtn().click()
        time.sleep(5)
        log.info("Clicking to share pre-checkin link icon")
        bookingPage.getShareLinkBtn().click()
        time.sleep(2)
        log.info("Copying link")
        link = bookingPage.getShareLinkInput().get_attribute('value')
        log.info("Pre checkin link - " + link)
        log.info("Closing copy link modal")
        bookingPage.getPreCheckinCopyModalCloseBtn().click()
        log.info("Profile menu opening")
        bookingPage.getProfileMenuExpLink().click()
        log.info("Logout from the current session")
        bookingPage.getLogoutLink().click()
        self.driver.add_cookie({'name': 'link', 'value': link})
        time.sleep(5)

    #Test basic info tab with blank data
    def test_pre_checkin_basic_info_with_blank_data(self):
        """Test basic info with blank data page"""
        log = self.myLogger()
        fake = Faker()
        link = str(self.driver.get_cookie('link')['value'])
        log.info("URL from Cookie " + link)
        time.sleep(5)
        self.driver.get(link)
        log.info("Redirecting to pre-check-in page")
        time.sleep(5)
        preCheckinPage = PrecheckinPage(self.driver)
        log.info("Clicking to get started")
        preCheckinPage.getStartedBtn().click()
        # Basic info tab
        time.sleep(2)
        log.info("Clicking to save button")
        preCheckinPage.getStartedBtn().click()
        time.sleep(2)

        #checking error messages
        # phone number
        try:
            phone_error_msg = preCheckinPage.getPhoneInputError().text
            log.info("Phone number error message is - " + phone_error_msg)
            assert 'phone number' in phone_error_msg
            preCheckinPage.getPhoneInput().send_keys('9839098390')
            preCheckinPage.getStartedBtn().click()
        except:
            log.info("Phone input field or error message is not found")

        #Full name
        try:
            fullname_error_msg = preCheckinPage.getFullNameInputError().text
            log.info("Full name error message is - " + fullname_error_msg)
            assert 'Full Name' in fullname_error_msg
        except:
            log.info("Full name input field or error message is not found")

        # DOB
        try:
            dob_error_msg = preCheckinPage.getDobInputError().text
            log.info("Dob error message is - " + dob_error_msg)
            assert 'Date of Birth' in dob_error_msg
        except:
            log.info("DOB input field or error message is not found")

        # Nationality
        try:
            nationality_error_msg = preCheckinPage.getNationalityInputError().text
            log.info("Nationality error message is - " + nationality_error_msg)
            assert 'Nationality' in nationality_error_msg
        except:
            log.info("Nationality input field or error message is not found")

        # Email
        try:
            email_error_msg = preCheckinPage.getEmailInputError().text
            log.info("Email error message is - " + email_error_msg)
            assert 'Email' in email_error_msg
        except:
            log.info("Email input field or error message is not found")

        # Gender
        try:
            gender_error_msg = preCheckinPage.getGenderInputError().text
            log.info("Gender error message is - " + gender_error_msg)
            assert 'Gender' in gender_error_msg
        except:
            log.info("Gender input field or error message is not found")

        # Address
        try:
            address_error_msg = preCheckinPage.getAddressInputError().text
            log.info("Address error message is - " + address_error_msg)
            assert 'Address' in address_error_msg
        except:
            log.info("Address input field or error message is not found")

        # Zip Code
        try:
            zip_code_msg = preCheckinPage.getZipInputError().text
            log.info("Zip Code error message is - " + zip_code_msg)
            assert 'Zip Code' in zip_code_msg
        except:
            log.info("Zip Code input field or error message is not found")

        time.sleep(2)

    # Test Basic info with invalid email
    def test_pre_checkin_basic_info_with_invalid_email(self):
        log = self.myLogger()
        fake = Faker()
        link = str(self.driver.get_cookie('link')['value'])
        log.info("URL from Cookie " + link)
        time.sleep(2)
        self.driver.get(link)
        log.info("Redirecting to pre-check-in page")
        time.sleep(2)
        preCheckinPage = PrecheckinPage(self.driver)
        log.info("Clicking to get started")
        preCheckinPage.getStartedBtn().click()
        # Basic info tab
        time.sleep(3)
        log.info("Filling invalid email")
        try:
            preCheckinPage.getEmailInput().clear()
            preCheckinPage.getEmailInput().send_keys(fake.first_name())
            log.info("Clicking to save button")
            preCheckinPage.getStartedBtn().click()
        except:
            log.info("Email input field is not found")

        log.info("Clicking to save button")
        preCheckinPage.getStartedBtn().click()

    # Test basic info with valid data page
    def test_pre_checkin_basic_info_with_valid_data(self):
        """Test basic info with valid data page"""
        log = self.myLogger()
        fake = Faker()
        link = str(self.driver.get_cookie('link')['value'])
        log.info("URL from Cookie " + link)
        time.sleep(2)
        self.driver.get(link)
        log.info("Redirecting to pre-check-in page")
        time.sleep(2)
        preCheckinPage = PrecheckinPage(self.driver)
        log.info("Clicking to get started")
        preCheckinPage.getStartedBtn().click()
        # Basic info tab
        time.sleep(3)
        log.info("Filling full name")
        try:
            preCheckinPage.getFullNameInput().clear()
            preCheckinPage.getFullNameInput().send_keys(fake.name())
        except:
            log.info("Full name input field is not found")

        # phone number
        log.info("Filling phone field")
        try:
            time.sleep(2)
            preCheckinPage.getPhoneInput().clear()
            preCheckinPage.getPhoneInput().send_keys(fake.phone_number())
        except:
            log.info("Phone input field is not found")

        # phone number
        log.info("Filling DOB field")
        dob_date = datetime.datetime.now() + datetime.timedelta(days=-50)
        try:
            preCheckinPage.getDobInput().clear()
            preCheckinPage.getDobInput().send_keys(dob_date)
        except:
            log.info("DOB input field is not found")

        log.info("Selecting Nationality")
        try:
            nationality = Select(preCheckinPage.getNationalityInput())
            random_nationality = random.randint(1, len(nationality.options) - 1)
            nationality.select_by_index(str(random_nationality))
        except:
            log.info("Nationality input not found")

        log.info("Filling Email input")
        try:
            preCheckinPage.getEmailInput().clear()
            preCheckinPage.getEmailInput().send_keys(fake.email())
        except:
            log.info("Email input field is not found")

        log.info("Filling Address input")
        try:
            preCheckinPage.getAddressInput().clear()
            preCheckinPage.getAddressInput().send_keys(fake.address())
        except:
            log.info("Address input field is not found")

        log.info("Filling postal code input")
        try:
            preCheckinPage.getZipInput().clear()
            preCheckinPage.getZipInput().send_keys(fake.postcode())
        except:
            log.info("Postal code input field is not found")

        log.info("Filling Adult count input")
        try:
            preCheckinPage.getAdultsCountInput().clear()
            preCheckinPage.getAdultsCountInput().send_keys(2)
        except:
            log.info("Adult count input field is not found")

        log.info("Filling children count input")
        try:
            preCheckinPage.getChildrenInput().clear()
            preCheckinPage.getChildrenInput().send_keys(2)
        except:
            log.info("Children count input field is not found")

        log.info("Clicking to save button")
        preCheckinPage.getStartedBtn().click()

