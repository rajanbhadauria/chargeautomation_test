from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def loginBtn(self):
        return self.driver.find_element(By.LINK_TEXT, 'LOG IN')

    def signupBtn(self):
        return self.driver.find_element(By.XPATH, "//a[contains(@href, '/register')]")


        

