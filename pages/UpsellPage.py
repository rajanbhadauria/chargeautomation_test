from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utilities.BaseClass import BaseClass


class UpsellPage:

    def __init__(self, driver):
        self.driver = driver

    def upsellLink(self):
        baseClass = BaseClass()
        return baseClass.verify_element_presence(self.driver, By.LINK_TEXT, 'Upsell')

    def manageUpsellLink(self):
        baseClass = BaseClass()
        return baseClass.verify_element_presence(self.driver, By.LINK_TEXT, 'Manage Upsell')

    def upsellTabLinks(self):
        return self.driver.find_elements(By.XPATH, "//a[contains(@class, 'upsell-tab-nav-pill')]")

    def upsellCounts(self):
        return self.driver.find_element(By.XPATH, '//h1/span')

    def getAllPages(self):
        return self.driver.find_elements(By.XPATH, "//li[contains(@class, 'page-item')]")

    def getAllUpsellRowsInPage(self):
        return self.driver.find_elements(By.XPATH, "//div[contains(@class, 'property-card upsell')]")

    def getHelpLinkTooltip(self):
        return self.driver.find_element(By.XPATH, "//a[@class='help-link']")

    def getHelpTooltip(self):
        return self.driver.find_element(By.XPATH, "//div[@class='tooltip-inner']")

    def getHelpLink(self):
        return self.driver.find_element(By.LINK_TEXT, "Learn More")

    def getHelpPageTitle(self):
        return self.driver.find_element(By.XPATH, "//h1")

    def getCreateUpsellBtn(self):
        return self.driver.find_element(By.ID, "add-upsell-btn")

    def getBlankTemplateLink(self):
        return self.driver.find_element(By.XPATH, "//a[@class='temp-box start']")

    def getTitleInput(self):
        return self.driver.find_element(By.ID, "upsellTitle")

    def getPriceInput(self):
        return self.driver.find_element(By.ID, "new_add_on_upsell_price")

    def getPriceModalSelectBox(self):
        return Select(self.driver.find_element(By.ID, "new_add_on_upsell_per"))

    def getSaveUpsellBtn(self):
        return self.driver.find_element(By.XPATH, "//button[contains(@class, 'save-upsell')]")

    def getTitleInputErrorMsg(self):
        return self.driver.find_element(By.XPATH, "//input[@id='upsellTitle']/following-sibling::small/strong")

    def getPriceInputErrorMsg(self):
        return self.driver.find_element(By.XPATH, "//input[@id='new_add_on_upsell_price']/../../small/strong")

    def getCloseModalBtn(self):
        return self.driver.find_element(By.ID, "close-upsell-modal")

    def alertModalMsg(self):
        return self.driver.find_element(By.ID, "swal2-content")





