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

    def menuListButton(self):
        return self.driver.find_element(By.XPATH, "//button[contains(@class, 'dropdown-toggle-split')]")

    def createPaymentLink(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "dropdown-menu-right show")]/a[1]')

    def chargePaymentLink(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "dropdown-menu-right show")]/a[2]')

    def scheduleChargeLink(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "dropdown-menu-right show")]/a[3]')

    def selectPaymentMethod(self):
        return self.driver.find_elements(By.XPATH, "//select[@id='chargePaymentMethod']/option")

    def addPaymentMethod(self):
        return self.driver.find_element(By.XPATH, "//a[@href='#newPaymentMethod']")

    def nameOnCard(self):
        return self.driver.find_element(By.ID, "full_name")

    # def stripeIframe(self):
    #     return self.driver.find_element(By.XPATH, "//div[@id='card-element']//iframe")

    def addCard(self, card_data):
        iframe = self.driver.find_element(By.XPATH, "//div[@id='card-element']//iframe")
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(By.NAME, 'cardnumber').send_keys(card_data)


    def backToMainContent(self):
        self.driver.switch_to.default_content()

    def chargeNowBtn(self):
        return self.driver.find_element(By.XPATH, "//div[@id='paymentChargeModal']//a[contains(@class, 'btn-primary')]")

    def paymentSuccessMessage(self):
        baseClass = BaseClass()
        return baseClass.verify_element_presence(self.driver, By.XPATH, "//div[@class='toast toast-success']/div")

    def paymentStatusLabel(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'form-row')]//span[contains(@class,'badge')]")

    def fullNameError(self):
        return self.driver.find_element(By.XPATH, "//input[@id='full_name']/following-sibling::span")

    def scheduleDateError(self):
        return self.driver.find_element(By.XPATH, "//small")

    def emailInput(self):
        return self.driver.find_element(By.ID, 'transactionContact')

    def emailError(self):
        return self.driver.find_element(By.XPATH, "//input[@id= 'transactionContact']/parent::div/small/strong")

    def amountInput(self):
        return self.driver.find_element(By.XPATH, "//div[@class='input-group currency-box']/input")

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

    def newRequestBtns(self):
        return self.driver.find_elements(By.XPATH, "//a[contains(@class, 'add-request')]")

    def toggleRowButtons(self):
        return self.driver.find_elements(By.XPATH, "//a[@class='card-collapse collapsed']")

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
        return self.driver.find_element(By.XPATH, "//label[@for='create-payment-request-cb-toggle']")

    def closeRequestModalButton(self):
        return self.driver.find_element(By.ID, "closeAddEditPaymentRequestButton")

    def copyLinkCloseBtn(self):
        return self.driver.find_element(By.XPATH, "//div[@id='paymentRequestLinkModal']//a")

    def selectExpiryDateButton(self):
        return self.driver.find_element(By.XPATH, "//div[@id='date_2-wrapper']//button[contains(@class, 'validate')]")

    def expiryDateInput(self):
        return self.driver.find_element(By.ID, 'date_2-input')

    def sentLinkSuccessMessage(self):
        baseClass = BaseClass()
        return baseClass.verify_element_presence(self.driver, By.XPATH, "//div[@id='paymentLinkSentModal']//h4")

    def createLinkSuccessMessage(self):
        baseClass = BaseClass()
        return baseClass.verify_element_presence(self.driver, By.XPATH, "//div[@id='paymentLinkCreatedModal']//h4")

    def getPaymentRequestLink(self):
        return self.driver.find_element(By.ID, 'paymentLinkSentModal_linkCopyInput')

    def closeModalBtn(self):
        return self.driver.find_element(By.XPATH, "//div[@id='paymentLinkSentModal']//a[contains(@class, 'btn-sm')]")

    def closeChargeNowBtn(self):
        return self.driver.find_element(By.ID, "closeChargeNowModal")

    def closeSentLinkModalBtn(self):
        return self.driver.find_element(By.ID, 'close_sentLinkModal')

    def expandMenuListBtn(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'option-column')]/div")

    def toastSuccessMessage(self):
        baseClass = BaseClass()
        return baseClass.verify_element_presence(self.driver, By.XPATH, "//div[@id='toast-container']/div/div")
    def copyLinkInput(self):
        return self.driver.find_element(By.ID, 'paymentRequestLinkModal_linkCopyInput')

    def findAllExpandMenuLinks(self):
        return self.driver.find_elements(By.XPATH, "//div[contains(@class, 'option-column')]/div/div/a")

    def confirmModalBtn(self):
        return self.driver.find_element(By.XPATH, "//div[@class = 'swal2-actions']/button[1]")

    def filterInput(self):
        return self.driver.find_element(By.ID, "filter-search")

    def findRequestRows(self):
        return self.driver.find_elements(By.XPATH, "//div[contains(@class, 'payment-request-pane')]")

    def findRequestType(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'form-row')]/div[contains(@class, 'col-1 col-xs-6')]/span")

    def findAmount(self):
        return self.driver.find_element(By.XPATH, "//span[contains(@class, 'payment-amount-label')]")

    def findRequestIdLabel(self):
        return self.driver.find_element(By.XPATH, "//span[contains(@class, 'payment-id-label')]")

    def findEmail(self):
        return self.driver.find_element(By.XPATH, "//span[contains(@class, 'payment-email-label')]")

    def findShieldIcon(self):
        return self.driver.find_element(By.XPATH, "//span/i[@class='fas fa-shield-alt text-muted']")

    def findPaidOnDate(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'form-row')]/div[contains(@class, 'col-6')][1]/dl/dd")

    def findScheduleDateLabel(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'form-row')]/div[contains(@class, 'col-6')][2]/dl/dd")

    def findExpiryDateLabel(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'form-row')]/div[contains(@class, 'col-6')][3]/dl/dd")

    def findChargebackProtectionLabel(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'form-row')]/div[contains(@class, 'col-6')][4]/dl/dd")

    def findPaymentMethodLabel(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'form-row')]/div[contains(@class, 'col-6')][5]/dl/dd")

    def findDescription(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'collapse')]//div[@class='row form-row']/div[@class = 'col-12 col-md-5']//dd")

    def findTerms(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'collapse')]//div[@class='row form-row']/div[@class = 'col-12 col-md-4']//dd")

    def findReferenceNumber(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'collapse')]//div[@class='row form-row']/div[@class = 'col-12 col-md-3']//dd")



