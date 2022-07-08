import time
from faker import Faker
import random
import pytest

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.PaymentPagesPage import PaymentPagesPage
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures('loginData')
class TestPaymentPages(BaseClass):

    # Login to site
    def test_login(self, loginData):
        """Test Payment request login to charge automation"""
        log = self.myLogger()
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        paymentPages = PaymentPagesPage(self.driver)
        log.info("Clicking to login link")
        homePage.loginBtn().click()
        log.info("Filling login form")
        loginPage.emailInput().send_keys(loginData['email'])
        log.info("Login email - " + f"'{loginPage.emailInput().get_attribute('value')}'")
        loginPage.passwordInput().send_keys(loginData['password'])
        log.info("Login password - " + f"'{loginPage.passwordInput().get_attribute('value')}'")
        loginPage.loginSubmitBtn().click()
        time.sleep(2)
        log.info("Redirecting manage payment request link")
        paymentPages.paymentPagesLink().click()
        paymentPages.paymentPagesManageLink().click()
        time.sleep(2)

    #create payment page with blank data
    def test_create_payment_page_with_blank_data(self):
        """Creating payment page with blank data"""
        paymentPage = PaymentPagesPage(self.driver)
        log = self.myLogger()
        log.info("Redirecting to create payment page")
        paymentPage.createPaymentPageLink().click()
        time.sleep(2)
        paymentPage.addEditPageSubmitBtn().click()
        product_error_message = paymentPage.productErrorMsg().text
        assert('select product' in product_error_message)
        log.info("Product error message is - "+product_error_message)

    #create product from create payment page with blank data
    def test_create_product_with_blank_data_on_create_payment_page(self):
        """Create product from create payment page with blank data"""
        log = self.myLogger()
        paymentPage = PaymentPagesPage(self.driver)
        paymentPage.createPaymentPageLink().click()
        log.info("Opening product list select box")
        paymentPage.productSelectBox().click()
        log.info('Clicking to add product')
        paymentPage.addProductLinkInSelectBox().click()
        log.info("Clicking Save Button")
        paymentPage.saveProductBtnOnModal().click()
        time.sleep(2)
        errorMsg = paymentPage.productNameErrorOnModal().text
        log.info("Product error message is - " + errorMsg)
        assert ("The name" in errorMsg)

    # create product from create payment page with long description data
    def test_create_product_with_long_description_on_create_payment_page(self):
        """create product from create payment page with long description data"""
        log = self.myLogger()
        paymentPage = PaymentPagesPage(self.driver)
        fake = Faker()
        product_name = fake.name()
        product_price = str(random.randint(50, 100))
        product_currency = paymentPage.productSelectedCurrency().get_attribute("alt")
        product_description = ""
        for _ in range(10):
            product_description += fake.paragraph(nb_sentences=5)
        paymentPage.createPaymentPageLink().click()
        log.info("Opening product list select box")
        paymentPage.productSelectBox().click()
        log.info('Clicking to add product')
        paymentPage.addProductLinkInSelectBox().click()
        log.info("Putting product name : " + product_name)
        paymentPage.productNameInput().send_keys(product_name)
        log.info("Putting product price : " + product_price)
        paymentPage.productAmountInput().send_keys(product_price)
        log.info("Putting product description : " + product_description)
        paymentPage.productDescriptionInput().send_keys(product_description)
        log.info("Clicking Save Button")
        paymentPage.saveProductBtnOnModal().click()
        time.sleep(2)
        errorMsg = paymentPage.productDescriptionErrorOnModal().text
        log.info("Product description error message is - " + errorMsg)
        assert ("description may not be greater" in errorMsg)

    # create product with vaild data from create payment page
    def test_create_product_with_valid_data_on_create_payment_page(self):
        """Create product from create payment page with valid data"""
        log = self.myLogger()
        fake = Faker()
        paymentPage = PaymentPagesPage(self.driver)

        product_name = fake.name()
        product_price = str(random.randint(50, 100))
        product_currency = paymentPage.productSelectedCurrency().get_attribute("alt")
        product_description = ""
        product_description += fake.paragraph(nb_sentences=5)

        paymentPage.createPaymentPageLink().click()
        log.info("Opening product list select box")
        paymentPage.productSelectBox().click()
        log.info('Clicking to add product')
        paymentPage.addProductLinkInSelectBox().click()

        log.info("Putting product name : "+product_name)
        paymentPage.productNameInput().send_keys(product_name)
        log.info("Putting product price : " + product_price)
        paymentPage.productAmountInput().send_keys(product_price)
        log.info("Putting product description : " + product_description)
        paymentPage.productDescriptionInput().send_keys(product_description)
        log.info("Clicking Save Button")
        paymentPage.saveProductBtnOnModal().click()
        time.sleep(2)
        successMsg = paymentPage.productSuccessMsg().text
        log.info("Product success message " + successMsg)
        assert('Product added' in successMsg)
        log.info("Matching select product and created product")
        selectedProduct = paymentPage.selectedProductInput().text
        log.info("Supplied product : " + product_name)
        log.info("Selected product : " + selectedProduct)
        assert (selectedProduct == product_name)
        suppliedPrice = product_currency+product_price
        selectPrice = paymentPage.productPriceLabel().text
        log.info("Supplied product price: " + suppliedPrice)
        log.info("Selected product price: " + selectPrice)
        assert (suppliedPrice == suppliedPrice)


