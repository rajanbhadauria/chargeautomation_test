from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class PaymentRequestPage:

    def __init__(self, driver):
        self.driver = driver

    def paymentRequestLink(self):
        baseClass = BaseClass()
        return baseClass.verify_element_presence(self.driver, By.LINK_TEXT, 'Payment Request')
        # return self.driver.find_element(By.LINK_TEXT, 'Payment Request')

    def managePaymentRequestLink(self):
        baseClass = BaseClass()
        return baseClass.verify_element_presence(self.driver, By.XPATH, '//a[contains(@href, "payment-requests")]')
        #return self.driver.find_element(By.XPATH, '//a[contains(@href, "payment-requests")]')

    def addPaymentRequestLink(self):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Add New Request')

    def sendPaymentRequest(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'dropup')]/button[contains(@class, 'pl-3')]")

    def emailInput(self):
        return self.driver.find_element(By.ID, 'transactionContact')

    def emailError(self):
        return self.driver.find_element(By.XPATH, "//input[@id= 'transactionContact']/parent::div/small/strong")

    def amountInput(self):
        return self.driver.find_element(By.ID, 'transactionAmount')

    def selectCurrency(self):
        return self.driver.find_element(By.XPATH, "//div[@id='currency-selector']//img")

    def amountError(self):
        return self.driver.find_element(By.XPATH, "//input[@id= 'transactionAmount']/parent::div/parent::div/small/strong")

    def moreSettingsLink(self):
        return self.driver.find_element(By.XPATH, "//a[contains(@href, '#transactionSettings')]")

    def scheduleDateInput(self):
        return self.driver.find_element(By.ID, 'date_1-input')

    def scheduleDay(self, day):
        return self.driver.find_element(By.XPATH, "//div[@id='date_1-wrapper']//div[contains(@class, 'datepicker-days')]/button/span[contains(@class, 'datepicker-day-text') and text()="+str(day)+"]/parent::button")

    def scheduleHour(self, hour):
        return self.driver.find_element(By.XPATH, "//div[@id='date_1-wrapper']//div[contains(@class,'time-picker-column')][1]/div/button/span[contains(@class, 'time-picker-column-item-text') and text()="+str(hour)+"]")

    def scheduleMin(self, min):
        return self.driver.find_element(By.XPATH, "//div[@id='date_1-wrapper']//div[contains(@class,'time-picker-column')][2]/div/button/span[contains(@class, 'time-picker-column-item-text') and text()="+str(min)+"]")

    def scheduleDateError(self):
        return self.driver.find_element(By.XPATH, "//div[@id= 'date_1-wrapper']//parent::div/parent::div/small")

    def descriptionInput(self):
        return self.driver.find_element(By.ID, "transactionDescription")

    def termsInput(self):
        return self.driver.find_element(By.ID, "transactionTerms")

    def toggleRowButton(self):
        return self.driver.find_element(By.XPATH, "//a[contains(@class, 'card-collapse')]")

    def findDescription(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'collapse')]//div[@class='row form-row']/div[@class = 'col-12 col-md-5']//dd")

    def findTerms(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'collapse')]//div[@class='row form-row']/div[@class = 'col-12 col-md-4']//dd")

    def expiryDay(self, day):
        return self.driver.find_element(By.XPATH, "//div[@id='date_2-picker-container-DatePicker']//div[contains(@class, 'datepicker-days')]/button/span[contains(@class, 'datepicker-day-text') and text()="+str(day)+"]/parent::button[1]")

    def expiryHour(self, hour):
        return self.driver.find_element(By.XPATH, "//div[@id='date_2-wrapper']//div[contains(@class,'time-picker-column-hours')]//button/span[contains(@class, 'time-picker-column-item-text') and text()="+str(hour)+"]/parent::button[1]")

    def expiryMin(self, min):
        return self.driver.find_element(By.XPATH, "//div[@id='date_2-wrapper']//div[contains(@class,'time-picker-column-minutes')]//button/span[contains(@class,'time-picker-column-item-text') and text()="+str(min)+"][1]/parent::button[1]")

    def expiryDateError(self):
        return self.driver.find_element(By.XPATH, "//div[@id= 'date_2-wrapper']//parent::div/parent::div/small")


    def selectScheduleDateButton(self):
        return self.driver.find_element(By.XPATH, "//button[contains(@class, 'datepicker-button validate')][1]")

    def onChargeBackButton(self):
        return self.driver.find_element(By.XPATH, "//div[@class='checkbox-toggle checkbox-choice']/label")

    def closeRequestModalButton(self):
        return self.driver.find_element(By.ID, "closeAddEditPaymentRequestButton")

    def selectExpiryDateButton(self):
        return self.driver.find_element(By.XPATH, "//div[@id='date_2-wrapper']//button[contains(@class, 'validate')]")

    def expiryDateInput(self):
        return self.driver.find_element(By.ID, 'date_2-input')

    def sentLinkSuccessMessage(self):
        baseClass = BaseClass()
        return baseClass.verify_element_presence(self.driver, By.XPATH, "//div[@id='paymentLinkSentModal']//h4")

    def getPaymentRequestLink(self):
        return self.driver.find_element(By.ID, 'paymentLinkSentModal_linkCopyInput')

    def closeModalBtn(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'modal') and @style!='']// a[@data-dismiss = 'modal']")

    def filterInput(self):
        return self.driver.find_element(By.ID, "filter-search")

    def findRequestRows(self):
        return self.driver.find_elements(By.XPATH, "//div[contains(@class, 'payment-request-pane')]")

    def findAmount(self):
        return self.driver.find_element(By.XPATH, "//span[contains(@class, 'payment-amount-label')]")

    def findEmail(self):
        return self.driver.find_element(By.XPATH, "//span[contains(@class, 'payment-email-label')]")

    def findShieldIcon(self):
        return self.driver.find_element(By.XPATH, "//span/i[@class='fas fa-shield-alt text-muted']")




