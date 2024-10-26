from selenium import webdriver
from selenium.webdriver.common.by import By


class RegistrationPage:
    def __init__(self, driver):

        self.driver = driver;
        self.first_name = (By.ID, "input-firstname")
        self.last_name = (By.ID, "input-lastname")
        self.email = (By.ID, "input-email")
        self.phone_number = (By.ID, "input-telephone")
        self.pass_word = (By.ID, "input-password")
        self.pass_confirm = (By.ID, "input-confirm")
        self.agree_terms = (By.XPATH, "//input[@name='agree']")
        self.continue_button = (By.XPATH,"//input[@value='Continue']")

    def set_Firstname(self, fname):
        self.driver.find_element(*self.first_name).send_keys(fname)

    def set_lastname(self, lname):
        self.driver.find_element(*self.last_name).send_keys(lname)

    def set_email(self, email):
        self.driver.find_element(*self.email).send_keys(email)

    def set_phonenumber(self, number):
        self.driver.find_element(*self.phone_number).send_keys(number)

    def set_password(self, password):
        self.driver.find_element(*self.pass_word).send_keys(password)

    def confirm_password(self, password):
        self.driver.find_element(*self.pass_confirm).send_keys(password)

    def agree_termsAndCon(self):
        self.driver.find_element(*self.agree_terms).click()

    def clickOnContinue(self):
        self.driver.find_element(*self.continue_button).click()

