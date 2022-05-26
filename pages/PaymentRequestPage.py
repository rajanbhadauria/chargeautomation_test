from selenium.webdriver.common.by import By

class PaymentRequestPage:

    def __init__(self, driver):
        self.driver = driver

    def managePaymentRequestLink(self):
        return self.driver.find_element(By.XPATH, '//a[contains(@href, "payment-requests")]')

