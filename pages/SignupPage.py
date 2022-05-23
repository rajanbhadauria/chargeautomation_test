from selenium.webdriver.common.by import By


class SignupPage:

    def __init__(self, driver):
        self.driver = driver

    def fullName(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Full Name']")

    def fullNameError(self):
        return self.driver.find_element(By.XPATH, "//div[@class='user']//span[contains(@class,'invalid-feedback')][1]")

    def companyName(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Company Name']")

    def companyNameError(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'company')]//span[contains(@class,'invalid-feedback')]/span")

    def phone(self):
        return self.driver.find_element(By.XPATH, "//input[@type='tel']")

    def phoneError(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'phone')]//span[contains(@class,'invalid-feedback')]/span")

    def email(self):
        return self.driver.find_element(By.XPATH, "//input[@type='email']")

    def emailError(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'email')]//span[contains(@class,'invalid-feedback')]/span")

    def password(self):
        return self.driver.find_element(By.ID, "password")

    def confirm_password(self):
        return self.driver.find_element(By.ID, "password-confirm")

    def pms(self):
        return self.driver.find_element(By.XPATH, "//div[@class='network']//input")

    def agree(self):
        return self.driver.find_element(By.XPATH, "//span[@class='checkmark']")

    def signupSubmit(self):
        return self.driver.find_element(By.ID, "signupbtn")







