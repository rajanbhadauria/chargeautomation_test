from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utilities.BaseClass import BaseClass


class BookingPage:

    def __init__(self, driver):
        self.driver = driver
        self.baseClass = BaseClass()

    def bookingLink(self):
        return self.baseClass.verify_element_presence(self.driver, By.LINK_TEXT, 'Bookings')

    def getNewbookingBtn(self):
        return self.driver.find_element(By.ID, 'add_booking_button')

    def getRentalDropdown(self):
        return self.driver.find_element(By.ID, 'assigned_rental')

    def getBookingSourceDropdown(self):
        return self.driver.find_element(By.ID, 'booking_source')

    def getBookingAmountInput(self):
        return self.driver.find_element(By.ID, 'total_booking_amount')

    def getFirstNameInput(self):
        return self.driver.find_element(By.ID, 'first_name')

    def getLastNameInput(self):
        return self.driver.find_element(By.ID, 'last_name')

    def getEmailInput(self):
        return self.driver.find_element(By.ID, 'email')

    def getSubmitBookingBtn(self):
        return self.driver.find_element(By.XPATH, "//div[@id='add_edit_booking_modal']//button[contains(@class, 'btn-success')][1]")

    def getDateInput(self):
        return self.driver.find_element(By.XPATH, "//div[@id='datepicker-trigger-booking-add']")

    def getCalendarDate(self, date_supplied):
        print("#######################")
        print("//div[@id='airbnb-style-datepicker-wrapper-3fUnU']//td[@data-date='"+date_supplied+"']")
        print("#######################")
        return self.driver.find_element(By.XPATH, "//div[@class='asd__month'][1]//td/button[@date='"+date_supplied+"'][1]")

    def getSaveBookingBtn(self):
        return self.driver.find_element(By.XPATH, "//div[@id='add_edit_booking_modal']//button[@name='Save Changes'][1]")







