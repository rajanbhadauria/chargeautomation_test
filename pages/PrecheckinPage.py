from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utilities.BaseClass import BaseClass


class PrecheckinPage:

    def __init__(self, driver):
        self.driver = driver
        self.baseClass = BaseClass()

    def getStartedBtn(self):
        return self.driver.find_element(By.XPATH, "//a[contains(@class, 'btn-success')]")

    ## Basic info page elements
    def getFullNameInput(self):
        return self.driver.find_element(By.ID, 6)

    def getPhoneInput(self):
        return self.driver.find_element(By.ID, "phone-6xunt6")

    def getDobInput(self):
        return self.driver.find_element(By.ID, "7")

    def getNationalityInput(self):
        return self.driver.find_element(By.ID, "8")

    def getEmailInput(self):
        return self.driver.find_element(By.ID, "1")

    def getGenderInput(self):
        return self.driver.find_element(By.ID, "9")

    def getAddressInput(self):
        return self.driver.find_element(By.ID, "update-property-address")

    def getZipInput(self):
        return self.driver.find_element(By.ID, "11")

    def getAdultsCountInput(self):
        return self.driver.find_element(By.ID, "guestAdults")

    def getChildrenInput(self):
        return self.driver.find_element(By.ID, "guestChildren")



