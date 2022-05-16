from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def emailInput(self):
        return self.driver.find_element(By.XPATH, "//input[@type='email']")

    def passwordInput(self):
        return self.driver.find_element(By.XPATH, "//input[@type='password']")

    def rememberInput(self):
        return self.driver.find_element(By.CSS_SELECTOR, "label.remember-login>input")

    def loginSubmitBtn(self):
        return self.driver.find_element(By.ID, "loginbtn")

    def dashbordLink(self):
        return self.driver.find_element(By.XPATH, '//a[contains(@href,"dashboard")]')

    def emailError(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[class='group'] span span")

    def passwordError(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[class='group has-error'] span span")

