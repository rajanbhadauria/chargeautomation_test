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
