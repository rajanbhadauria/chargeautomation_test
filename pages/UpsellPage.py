from selenium.webdriver.common.by import By

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

    def upsellCounts(self):
        return self.driver.find_element(By.XPATH, '//h1/span')

    def getAllPages(self):
        return self.driver.find_elements(By.XPATH, "//li[contains(@class, 'page-item')]")

    def getAllUpsellRowsInPage(self):
        return self.driver.find_elements(By.XPATH, "//div[contains(@class, 'property-card upsell')]")




