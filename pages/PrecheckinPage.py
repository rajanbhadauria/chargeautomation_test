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
        return self.baseClass.verify_element_presence(self.driver, By.ID, 6)

    def getPhoneInput(self):
        return self.baseClass.verify_element_presence(self.driver, By.XPATH, "//input[@type='tel']")

    def getDobInput(self):
        return self.baseClass.verify_element_presence(self.driver, By.ID, "7")

    def getNationalityInput(self):
        return self.baseClass.verify_element_presence(self.driver, By.ID, "8")

    def getEmailInput(self):
        return self.baseClass.verify_element_presence(self.driver, By.ID, "1")

    def getGenderInput(self):
        return self.baseClass.verify_element_presence(self.driver, By.ID, "9")

    def getAddressInput(self):
        return self.baseClass.verify_element_presence(self.driver, By.ID, "update-property-address")

    def getZipInput(self):
        return self.baseClass.verify_element_presence(self.driver, By.ID, "11")

    def getAdultsCountInput(self):
        return self.baseClass.verify_element_presence(self.driver, By.ID, "guestAdults")

    def getChildrenInput(self):
        return self.baseClass.verify_element_presence(self.driver, By.ID, "guestChildren")



