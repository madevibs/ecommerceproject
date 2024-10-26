
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):

        self.driver=driver;
        self.my_account=(By.XPATH,"//a[@title='My Account']")
        self.login=(By.XPATH,"//a[normalize-space()='Login']")
        self.register=(By.XPATH,"//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Register']")

    def clickonMyaccount(self):
        self.driver.find_element(*self.my_account).click()

    def clickOnLogin(self):
        self.driver.find_element(*self.login).click()

    def clickOnRegister(self):
        self.driver.find_element(*self.register).click()

