from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utilities.BaseClass import BaseClass


class PrecheckinPage:

    def __init__(self, driver):
        self.driver = driver
        self.baseClass = BaseClass()

    def getSuccessMessage(self):
        return self.baseClass.verify_element_presence(self.driver, By.XPATH, "//div[@class='toast toast-success']/div")

    def getStartedBtn(self):
        return self.driver.find_element(By.XPATH, "//a[contains(@class, 'btn-success')]")

    ## get current tab title
    def getActiveTabTitle(self):
        return self.driver.find_element(By.XPATH, "//a[@class='gp-step active']/span[contains(@class, 'd-none')]")

    ## Basic info page elements
    def getFullNameInput(self):
        return self.baseClass.verify_element_presence(self.driver, By.ID, 6)

    def getFullNameInputError(self):
        return self.driver.find_element(By.XPATH, '//input[@id="6"]/parent::div/following-sibling::small')

    def getPhoneInput(self):
        return self.baseClass.verify_element_presence(self.driver, By.XPATH, "//input[@type='tel']")

    def getPhoneInputError(self):
        return self.driver.find_element(By.XPATH, "//div[@class='custom-phone-input']/following-sibling::small")

    def getDobInput(self):
        return self.baseClass.verify_element_presence(self.driver, By.ID, "7")

    def getDobInputError(self):
        return self.driver.find_element(By.XPATH, "//input[@id='7']/parent::div/following-sibling::small")

    def getNationalityInput(self):
        return self.baseClass.verify_element_presence(self.driver, By.ID, "8")

    def getNationalityInputError(self):
        return self.driver.find_element(By.XPATH, "//select[@id='8']/parent::div/following-sibling::small")

    def getEmailInput(self):
        return self.baseClass.verify_element_presence(self.driver, By.ID, "1")

    def getEmailInputError(self):
        return self.driver.find_element(By.XPATH, "//input[@id='1']/parent::div/following-sibling::small")

    def getGenderInput(self):
        return self.baseClass.verify_element_presence(self.driver, By.ID, "9")

    def getGenderInputError(self):
        return self.driver.find_element(By.XPATH, "//select[@id='9']/parent::div/following-sibling::small")

    def getAddressInput(self):
        return self.baseClass.verify_element_presence(self.driver, By.ID, "update-property-address")

    def getAddressInputError(self):
        return self.driver.find_element(By.XPATH, "//input[@id='update-property-address']/following-sibling::small")

    def getZipInput(self):
        return self.baseClass.verify_element_presence(self.driver, By.ID, "11")

    def getZipInputError(self):
        return self.driver.find_element(By.XPATH, "//input[@id='11']/parent::div/following-sibling::small")

    def getAdultsCountInput(self):
        return self.baseClass.verify_element_presence(self.driver, By.ID, "guestAdults")

    def getChildrenInput(self):
        return self.baseClass.verify_element_presence(self.driver, By.ID, "guestChildren")

    def getAllQuestionnaireFormInputs(self):
        return self.driver.find_elements(By.XPATH, '//form//input')

    def get3DSApprovalBtn(self):
        return self.driver.find_element(By.ID, 'test-source-authorize-3ds')



