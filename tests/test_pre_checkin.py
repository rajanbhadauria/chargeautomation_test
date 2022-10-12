import pytest
import time
import re
from faker import Faker

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from pages.UpsellPage import UpsellPage
from utilities.BaseClass import BaseClass
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage

@pytest.mark.usefixtures('loginData')
class TestUpsell(BaseClass):
    # Login to site
    def test_login(self, loginData):
        """Test Payment request login to charge automation"""
        log = self.myLogger()
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        upsellPage = UpsellPage(self.driver)
        log.info("Clicking to login link")
        homePage.loginBtn().click()
        log.info("Filling login form")
        loginPage.emailInput().send_keys(loginData['email'])
        log.info("Login email - " + f"'{loginPage.emailInput().get_attribute('value')}'")
        loginPage.passwordInput().send_keys(loginData['password'])
        log.info("Login password - " + f"'{loginPage.passwordInput().get_attribute('value')}'")
        loginPage.loginSubmitBtn().click()
        time.sleep(2)
        log.info("Redirecting manage upsell page")
        upsellPage.upsellLink().click()
        upsellPage.manageUpsellLink().click()

    # upsell count matching
    def test_upsell_count(self):
        """Match upsell counts"""
        upsellPage = UpsellPage(self.driver)
        log = self.myLogger()
        log.info("Get counts of upsell")
        try:
            upsellCount = re.sub('[^0-9a-zA-Z]+', '', upsellPage.upsellCounts().text)
        except NoSuchElementException:
            upsellCount = 0

        if upsellCount != 0:
            log.info("Total upsell count is as - " + upsellCount)
            maxPage = upsellPage.getAllPages()[-2].text
            log.info("Total page count is - " + maxPage)
            log.info("Loading last page")
            upsellPage.getAllPages()[-2].click()
            time.sleep(2)
            log.info("Counting all upsells in page ")
            totalItems = len(upsellPage.getAllUpsellRowsInPage())
            log.info(f"All upsells in page is {totalItems}")
            log.info("Matching upsell counts")
            total_upsell = ((int(maxPage)-1)*10) + totalItems
            assert total_upsell == int(upsellCount)
            log.info("Upsell count matched")
            log.info(f"Total upsell is - {total_upsell}")
        else:
            log.info("Upsell not found")

    # upsell help link testing
    def help_text_link(self):
        """Upsell help link testing"""
        log = self.myLogger()
        upsellPage = UpsellPage(self.driver)
        upsellPage.upsellTabLinks()[0].click()
        log.info("Clicking to help icon")
        upsellPage.getHelpLinkTooltip().click()
        helpTxt = upsellPage.getHelpTooltip().text
        log.info(f"Help text is - {helpTxt}")
        log.info("Clicking to Learn more link")
        log.info("Matching help page title")
        helpPageTitle = upsellPage.getHelpPageTitle().text
        assert('Upsell' in helpPageTitle)
        log.info(f"Help page title is - {helpPageTitle}")

    def close_and_switch(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])


    # create upsell with blank template and blank data
    def test_create_upsell_with_blank_template_and_data(self):
        """Create upsell with blank template and blank data"""
        log = self.myLogger()
        upsellPage = UpsellPage(self.driver)
        parentWindow = self.driver.current_window_handle
        log.info("Opening add upsell modal")
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(2)
        upsellPage.getCreateUpsellBtn().click()
        log.info("Opening blank template page")
        upsellPage.getBlankTemplateLink().click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        upsellPage.getPriceInput().send_keys(Keys.BACK_SPACE);
        log.info("Clicking to save")
        upsellPage.getSaveUpsellBtn().click()
        time.sleep(5)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.END)
        title_input_error_msg = upsellPage.getTitleInputErrorMsg().text
        log.info("Title error message is " + title_input_error_msg)
        price_input_error_msg = upsellPage.getPriceInputErrorMsg().text
        log.info("Price error message is " + price_input_error_msg)
        log.info("Matching Title error message ")
        assert("Title field" in title_input_error_msg)
        log.info("Matching Price error message ")
        assert ("The Price " in price_input_error_msg)
        self.close_and_switch()


    # Create upsell with blank template and invalid data
    def test_create_upsell_with_blank_template_and_invalid_data(self):
        """Create upsell with blank template and invalid data"""
        #self.driver.switch_to.window(self.driver.window_handles[0])
        log = self.myLogger()
        upsellPage = UpsellPage(self.driver)
        log.info("Opening blank template page")
        upsellPage.getBlankTemplateLink().click()
        log.info("Switching to add upsell template page")
        self.driver.switch_to.window(self.driver.window_handles[1])
        title_data = "-- javascript:void(0); <?php die();?> #//^&&3219 ,,-- +++++!`~~~"
        price_data = ""
        log.info('Filling title field')
        time.sleep(2)
        log.info("Wait for 2 seconds")
        upsellPage.getTitleInput().send_keys(title_data)
        log.info('Title data is -' + title_data)
        log.info('Filling price field')
        upsellPage.getPriceInput().send_keys(price_data)
        upsellPage.getPriceInput().send_keys(Keys.BACK_SPACE);
        log.info('Price data is -' + price_data)
        log.info("Clicking to save")
        element = upsellPage.getSaveUpsellBtn()
        element.click()
        log.info("Wait for 5 seconds ")
        time.sleep(5)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.END)
        price_input_error_msg = upsellPage.getPriceInputErrorMsg().text
        log.info("Matching Price error message ")
        log.info("Price error message is '" + price_input_error_msg + "'")
        assert ("The Price field is required" in price_input_error_msg)
        self.close_and_switch()


    # Create upsell with blank template and with blank price modal based on number of nights
    def test_create_upsell_with_blank_template_and_modal_based_per_night_and_blank_data(self):
        """Create upsell with blank template and with blank price modal based on number of nights"""
        log = self.myLogger()
        fake = Faker()
        upsellPage = UpsellPage(self.driver)
        upsellPage.getBlankTemplateLink().click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        title_data = fake.name()
        price_data = fake.pyint()
        log.info('Filling title field')
        upsellPage.getTitleInput().send_keys(title_data)
        log.info('Title data is -' + title_data)
        log.info('Changing price modal field')
        upsellPage.getPriceModalSelectBox().select_by_value("true")
        log.info('Price data is - Based on number of nights')
        log.info("Clicking to save")
        element = upsellPage.getSaveUpsellBtn()
        element.click()
        time.sleep(5)
        success_msg = upsellPage.alertModalMsg().text
        log.info("Success message is : " + success_msg)
        assert ("Upsell added successfully" in success_msg)
        self.close_and_switch()

    # Create upsell with blank template and valid data
    def test_create_upsell_with_blank_template_and_valid_data(self):
        """Create upsell with blank template and valid data"""
        log = self.myLogger()
        fake = Faker()
        upsellPage = UpsellPage(self.driver)
        upsellPage.getBlankTemplateLink().click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        title_data = fake.name()
        price_data = fake.pyint()
        log.info('Filling title field')
        upsellPage.getTitleInput().send_keys(title_data)
        log.info('Title data is -' + title_data)
        log.info('Filling price field')
        upsellPage.getPriceInput().send_keys(price_data)
        log.info('Price data is -' + str(price_data))
        log.info("Clicking to save")
        element = upsellPage.getSaveUpsellBtn()
        element.click()
        time.sleep(2)
        success_msg = upsellPage.alertModalMsg().text
        log.info("Success message is : " + success_msg)
        assert ("Upsell added successfully" in success_msg)
        self.close_and_switch()




