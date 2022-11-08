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
        random_rental = random.randint(1, len(rentals.options)-1)
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


    # Test landing to pre-checkin page
    def test_pre_checkin_landing(self):
        """Test landing to pre-checkin page"""
        log = self.myLogger()
        fake = Faker()
        link = str(self.driver.get_cookie('link')['value'])
        log.info("URL from Cookie " + link)
        time.sleep(2)
        self.driver.get(link)
        log.info("Redirecting to pre-check-in page")
        time.sleep(5)
        preCheckinPage = PrecheckinPage(self.driver)
        log.info("Clicking to get started")
        preCheckinPage.getStartedBtn().click()
        #Basic info tab
        time.sleep(5)
        log.info("Filling full name")
        try:
            preCheckinPage.getFullNameInput().send_keys(fake.name())
        except:
            log.info("Full name input field is not found")

        #phone number
        log.info("Filling phone field")
        try:
            preCheckinPage.getPhoneInput().send_keys(fake.phone())
        except:
            log.info("Phone input field is not found")

        # phone number
        log.info("Filling DOB field")
        dob_date = datetime.datetime.now() + datetime.timedelta(days=-50)
        try:
            preCheckinPage.getDobInput().send_keys(dob_date)
        except:
            log.info("DOB input field is not found")


        time.sleep(20)











