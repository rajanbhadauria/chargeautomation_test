import os
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
        #paymentPage.createPaymentPageLink().click()
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

    # create product from create payment page with large image
    def test_create_product_with_large_image_on_create_payment_page(self):
        """Create product from create payment page with large image"""
        log = self.myLogger()
        paymentPage = PaymentPagesPage(self.driver)
        fake = Faker()
        product_name = fake.name()
        product_price = str(random.randint(50, 100))
        product_currency = paymentPage.productSelectedCurrency().get_attribute("alt")
        product_description = ""
        for _ in range(10):
            product_description += fake.paragraph(nb_sentences=5)

        log.info("Putting product name : " + product_name)
        paymentPage.productNameInput().send_keys(product_name)
        log.info("Putting product price : " + product_price)
        paymentPage.productAmountInput().send_keys(product_price)
        log.info("Putting product description : " + product_description)
        paymentPage.productDescriptionInput().send_keys(product_description)
        log.info("Selecting image for upload")
        paymentPage.productImageInput().send_keys(os.getcwd()+"/images/15mb.jpeg")
        time.sleep(2)
        errorMsg = paymentPage.productSuccessMsg().text
        log.info("Image upload error message - " + errorMsg)
        assert('Image size' in errorMsg)
        log.info("Clicking Save Button")
        paymentPage.saveProductBtnOnModal().click()
        time.sleep(2)
        errorMsg = paymentPage.productDescriptionErrorOnModal().text
        log.info("Product description error message is - " + errorMsg)
        assert ("description may not be greater" in errorMsg)

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

        log.info("Putting product name : " + product_name)
        paymentPage.productNameInput().clear()
        paymentPage.productNameInput().send_keys(product_name)
        paymentPage.productDescriptionInput().clear()
        log.info("Putting product price : " + product_price)
        paymentPage.productAmountInput().send_keys(product_price)
        paymentPage.productDescriptionInput().clear()
        log.info("Putting product description : " + product_description)
        paymentPage.productDescriptionInput().send_keys(product_description)
        log.info("Clicking Save Button")
        paymentPage.saveProductBtnOnModal().click()
        time.sleep(2)
        errorMsg = paymentPage.productDescriptionErrorOnModal().text
        log.info("Product description error message is - " + errorMsg)
        assert ("description may not be greater" in errorMsg)

    # create product with valid data from create payment page
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

        log.info("Putting product name : "+product_name)
        paymentPage.productNameInput().clear()
        paymentPage.productNameInput().send_keys(product_name)
        log.info("Putting product price : " + product_price)
        paymentPage.productAmountInput().clear()
        paymentPage.productAmountInput().send_keys(product_price)
        log.info("Putting product description : " + product_description)
        paymentPage.productDescriptionInput().clear()
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

    # create product with valid image from create payment page
    def test_create_product_with_valid_image_on_create_payment_page(self):
        """Create product from create payment page with valid image"""
        log = self.myLogger()
        fake = Faker()
        paymentPage = PaymentPagesPage(self.driver)

        product_name = fake.name()
        product_price = str(random.randint(50, 100))
        product_currency = paymentPage.productSelectedCurrency().get_attribute("alt")
        product_description = ""
        product_description += fake.paragraph(nb_sentences=5)

        log.info("Opening product list select box")
        paymentPage.productSelectBox().click()
        log.info('Clicking to add product')
        paymentPage.addProductLinkInSelectBox().click()

        log.info("Putting product name : " + product_name)
        paymentPage.productNameInput().clear()
        paymentPage.productNameInput().send_keys(product_name)
        log.info("Putting product price : " + product_price)
        paymentPage.productAmountInput().clear()
        paymentPage.productAmountInput().send_keys(product_price)
        log.info("Putting product description : " + product_description)
        paymentPage.productDescriptionInput().clear()
        paymentPage.productDescriptionInput().send_keys(product_description)
        log.info("Selecting image for upload")
        paymentPage.productImageInput().send_keys(os.getcwd() + "/images/p1.jpg")
        time.sleep(2)
        log.info("Clicking Save Button")
        paymentPage.saveProductBtnOnModal().click()
        time.sleep(2)
        successMsg = paymentPage.productSuccessMsg().text
        log.info("Product success message " + successMsg)
        assert ('Product added' in successMsg)
        log.info("Matching select product and created product")
        selectedProduct = paymentPage.selectedProductInput().text
        log.info("Supplied product : " + product_name)
        log.info("Selected product : " + selectedProduct)
        assert (selectedProduct == product_name)
        suppliedPrice = product_currency + product_price
        selectPrice = paymentPage.productPriceLabel().text
        log.info("Supplied product price: " + suppliedPrice)
        log.info("Selected product price: " + selectPrice)
        assert (suppliedPrice == suppliedPrice)

    # create payment page without terms
    def test_create_payment_page_without_terms(self):
        """Create payment page without terms"""
        log = self.myLogger()
        fake = Faker()
        paymentPage = PaymentPagesPage(self.driver)

        product_name = fake.name()
        product_price = str(random.randint(50, 100))
        product_currency = paymentPage.productSelectedCurrency().get_attribute("alt")
        product_description = ""
        product_description += fake.paragraph(nb_sentences=5)

        #paymentPage.createPaymentPageLink().click()
        log.info("Opening product list select box")
        paymentPage.productSelectBox().click()
        log.info("Checking if product exists in the list")
        product_list = paymentPage.productSelectBoxList()
        if len(product_list) > 0:
            log.info("Product exists in the list")
            log.info("Selecting random product from the list")
            random_select = random.randint(0, len(product_list)-1)
            product_list[random_select].click()
            log.info("Select product is : " + paymentPage.selectedProductText().text)
        else:
            log.info('Clicking to add product')
            paymentPage.addProductLinkInSelectBox().click()
            log.info("Putting product name : " + product_name)
            paymentPage.productNameInput().send_keys(product_name)
            log.info("Putting product price : " + product_price)
            paymentPage.productAmountInput().send_keys(product_price)
            log.info("Putting product description : " + product_description)
            paymentPage.productDescriptionInput().send_keys(product_description)
            log.info("Selecting image for upload")
            paymentPage.productImageInput().send_keys(os.getcwd() + "/images/p1.jpg")
            time.sleep(2)
            log.info("Clicking Save Button")
            paymentPage.saveProductBtnOnModal().click()
            time.sleep(2)
            successMsg = paymentPage.productSuccessMsg().text
            log.info("Product success message " + successMsg)
            assert ('Product added' in successMsg)
            log.info("Matching select product and created product")
            selectedProduct = paymentPage.selectedProductInput().text
            log.info("Supplied product : " + product_name)
            log.info("Selected product : " + selectedProduct)
            assert (selectedProduct == product_name)
            suppliedPrice = product_currency + product_price
            selectPrice = paymentPage.productPriceLabel().text
            log.info("Supplied product price: " + suppliedPrice)
            log.info("Selected product price: " + selectPrice)
            assert (suppliedPrice == suppliedPrice)
        paymentPage.saveProductBtn().click()
        time.sleep(2)

    # create payment page with terms
    def test_create_payment_page_with_terms(self):
        """Test Create payment page with terms"""
        log = self.myLogger()
        fake = Faker()
        paymentPage = PaymentPagesPage(self.driver)
        terms = ""
        terms += fake.paragraph(nb_sentences=5)

        paymentPage.createPaymentPageLink().click()
        log.info("Opening product list select box")
        paymentPage.productSelectBox().click()
        log.info("Checking if product exists in the list")
        product_list = paymentPage.productSelectBoxList()
        log.info("Product exists in the list")
        log.info("Selecting random product from the list")
        random_select = random.randint(0, len(product_list)-1)
        product_list[random_select].click()
        log.info("Select product is : " + paymentPage.selectedProductText().text)
        log.info('Opening terms input')
        paymentPage.termsLink().click()
        log.info('Adding terms text to input')
        paymentPage.paymentPagesTermsInput().send_keys(terms)
        log.info('Terms text is : ' + terms)
        paymentPage.saveProductBtn().click()
        time.sleep(2)

    """Test edit payment page"""
    def test_edit_payment_pages(self):
        """Test edit payment page"""
        log = self.myLogger()
        fake = Faker()
        paymentPage = PaymentPagesPage(self.driver)
        log.info("Opening expand menu")
        paymentPage.paymentPagesListToggleMenu()[0].click()
        log.info("Clicking to edit payment page")
        paymentPage.editPaymentPageLink().click()
        log.info("Clicking to update booking button")
        paymentPage.addEditPageSubmitBtn().click()
        time.sleep(2)
        landedPage = paymentPage.managePaymentPageTitle().text
        log.info("Matching page title")
        assert('Manage Payment Pages', landedPage)
        log.info("Title is - " + landedPage)

    """Test view transaction link payment page"""
    def test_transaction_payment_pages(self):
        """Test view transaction link payment page"""
        log = self.myLogger()
        fake = Faker()
        paymentPage = PaymentPagesPage(self.driver)

        log.info("Opening expand menu")
        paymentPage.paymentPagesListToggleMenu()[0].click()
        log.info("Clicking to view txn page")
        paymentPage.viewTxnPaymentPageLink().click()
        time.sleep(2)
        landedPage = paymentPage.managePaymentPageTitle().text
        log.info("Matching page title")
        assert ('Transactions', landedPage)
        log.info("Title is - " + landedPage)

    """Test clone payment page"""
    def test_clone_payment_pages(self):
        """Test clone payment page"""
        log = self.myLogger()
        fake = Faker()
        paymentPage = PaymentPagesPage(self.driver)
        log.info("Opening manage page tab")
        paymentPage.managePageTabLink().click()
        log.info("Opening expand menu")
        paymentPage.paymentPagesListToggleMenu()[0].click()
        log.info("Clicking to clone page")
        paymentPage.clonePaymentPageLink().click()
        log.info("Clicking clone confirm button")
        paymentPage.cloneConfirmBtn().click()
        time.sleep(2)
        successMsg = paymentPage.productSuccessMsg().text
        log.info("Matching success message")
        assert ('Payment request page cloned successfully', successMsg)
        log.info("Success message - " + successMsg)

    """Test view payment page"""
    def test_view_payment_pages(self):
        """Test view payment page"""
        log = self.myLogger()
        fake = Faker()
        paymentPage = PaymentPagesPage(self.driver)
        log.info("Opening manage page tab")
        paymentPage.managePageTabLink().click()
        log.info("Opening expand menu")
        paymentPage.paymentPagesListToggleMenu()[0].click()
        log.info("Clicking to view page")
        paymentPage.viewPaymentPageLink().click()
        landedPage = paymentPage.managePaymentPageTitle().text
        log.info("Matching page title")
        assert ('', landedPage)
        log.info("Title is - " + landedPage)
        """Test clone payment page"""

    #Test copy link payment page
    def test_copy_link_payment_pages(self):
        """Test copy link payment page"""
        log = self.myLogger()
        fake = Faker()
        paymentPage = PaymentPagesPage(self.driver)
        log.info("Opening manage page tab")
        paymentPage.managePageTabLink().click()
        log.info("Opening expand menu")
        paymentPage.paymentPagesListToggleMenu()[0].click()
        log.info("Clicking to copy page")
        paymentPage.copyPaymentPageLink().click()
        time.sleep(2)
        successMsg = paymentPage.productSuccessMsg().text
        log.info("Matching success message")
        assert ('Payment page link copied to clipboard', successMsg)
        log.info("Success message - " + successMsg)

    #Test delete ayment page
    def test_delete_payment_pages(self):
        """Test delete payment page"""
        log = self.myLogger()
        fake = Faker()
        paymentPage = PaymentPagesPage(self.driver)
        log.info("Opening manage page tab")
        paymentPage.managePageTabLink().click()
        log.info("Opening expand menu")
        paymentPage.paymentPagesListToggleMenu()[0].click()
        log.info("Clicking to delete page")
        paymentPage.deletePaymentPageLink().click()
        log.info("Clicking delete confirm button")
        paymentPage.cloneConfirmBtn().click()
        time.sleep(2)
        successMsg = paymentPage.productSuccessMsg().text
        log.info("Matching success message")
        assert ('Payment request page deleted', successMsg)
        log.info("Success message - " + successMsg)





