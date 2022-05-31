from selenium.webdriver.common.by import By

class PaymentRequestPage:

    def __init__(self, driver):
        self.driver = driver

    def paymentRequestLink(self):
        return self.driver.find_element(By.LINK_TEXT, 'Payment Request')

    def managePaymentRequestLink(self):
        return self.driver.find_element(By.XPATH, '//a[contains(@href, "payment-requests")]')

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

    def amountError(self):
        return self.driver.find_element(By.XPATH, "//input[@id= 'transactionAmount']/parent::div/parent::div/small/strong")

    def moreSettingsLink(self):
        return self.driver.find_element(By.XPATH, "//a[contains(@href, '#transactionSettings')]")

    def scheduleDateInput(self):
        return self.driver.find_element(By.ID, 'date_1-input')

    def scheduleDay(self, day):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'datepicker-days')]/button/span[contains(@class, 'datepicker-day-text') and text()="+str(day)+"]/parent::button")

    def scheduleHour(self, hour):
        return self.driver.find_element(By.XPATH, "//div[contains(@class,'time-picker-column')][1]/div/button/span[contains(@class, 'time-picker-column-item-text') and text()="+str(hour)+"][1]")

    def scheduleMin(self, min):
        return self.driver.find_element(By.XPATH, "//div[contains(@class,'time-picker-column')][2]/div/button/span[contains(@class, 'time-picker-column-item-text') and text()="+str(min)+"][1]")

    def selectScheduleDateButton(self):
        return self.driver.find_element(By.XPATH, "//button[contains(@class, 'datepicker-button validate')][1]")


