from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_name = (By.ID, "input-email")
        self.pass_word = (By.ID, "input-password")
        self.login_button = (By.XPATH, "//input[@value='Login']")

    def enter_username(self, un):
        self.driver.find_element(*self.user_name).send_keys(un)

    def enter_password(self, pw):
        self.driver.find_element(*self.pass_word).send_keys(pw)

    def clickonLogin(self):
        self.driver.find_element(*self.login_button).click()
