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

    def productSelectBox(self):
        return self.driver.find_element(By.ID, "product-selector")

    def addProductLinkInSelectBox(self):
        return self.driver.find_element(By.XPATH, "//div[@id='product-selector']/div[@class='custom-dropdown-select-option_box']/a")

    def saveProductBtnOnModal(self):
        return self.driver.find_element(By.XPATH, "//div[@id='bookings-tabContent']//a[contains(@class, 'btn-success')]")

    def productNameErrorOnModal(self):
        return self.driver.find_element(By.XPATH, "//input[@id='transactionContact']/following-sibling::small")

    def productDescriptionErrorOnModal(self):
        return self.driver.find_element(By.XPATH, "//textarea[@id='transactionDescription']/following-sibling::small")

    def productNameInput(self):
        return self.driver.find_element(By.ID, "transactionContact")

    def productAmountInput(self):
        return self.driver.find_element(By.ID, "transactionAmount")

    def productDescriptionInput(self):
        return self.driver.find_element(By.ID, "transactionDescription")

    def productImageInput(self):
        return self.driver.find_element(By.ID, "reusable_product_image")

    def selectedProductInput(self):
        return self.driver.find_element(By.XPATH, "//div[@id = 'product-selector']//span")

    def productSuccessMsg(self):
        return self.driver.find_element(By.XPATH, "//div[@id='toast-container']//div[@class='toast-message']")

    def productPriceLabel(self):
        return self.driver.find_element(By.XPATH, "//div[@class='price notranslate']")

    def productSelectedCurrency(self):
        return self.driver.find_element(By.XPATH, "//div[@id='currency-selector']//img[1]")

    def productSelectBoxList(self):
        return self.driver.find_elements(By.XPATH, "//div[@id='product-selector']//ul/li")

    def productSelectBoxList(self):
        return self.driver.find_elements(By.XPATH, "//div[@id='product-selector']//ul/li")

    def selectedProductText(self):
        return self.driver.find_element(By.XPATH, "//div[@id='product-selector']//span")

    def saveProductBtn(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'payment-addedit-footer')]/button")

    def termsLink(self):
        return self.driver.find_element(By.ID, "rpp_tc")

    def paymentPagesTermsInput(self):
        return self.driver.find_element(By.ID, "reusable_payment_terms_and_conditions")

