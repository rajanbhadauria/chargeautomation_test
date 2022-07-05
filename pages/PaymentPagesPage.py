from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class PaymentPagesPage:

    def __init__(self, driver):
        self.driver = driver

    def paymentPagesLink(self):
        baseClass = BaseClass()
        return baseClass.verify_element_presence(self.driver, By.LINK_TEXT, 'Payment Pages')

    def paymentPagesManageLink(self):
        return self.driver.find_element(By.XPATH, "//a[contains(@href, 'reusable-payment-page-list')]")

    def createPaymentPageLink(self):
        return self.driver.find_element(By.XPATH, "//div[@class='req-btn-group']/a[contains(@href, 'reusable-payment-page')]")

    def addEditPageSubmitBtn(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'payment-addedit-footer')]/button")

    def productErrorMsg(self):
        return self.driver.find_element(By.XPATH, "//small[contains(@class, 'invalid-feedback')]/strong")
