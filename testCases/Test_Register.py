import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage
from pageObjects.RegistrationPage import RegistrationPage
from testCases.conftest import random_generator
from utilities.costomLogger import LogGen


class Test_register:
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_regster(self, set_up):
        self.logger.info("***entering homepage*******")

        hp = HomePage(set_up)
        hp.clickonMyaccount()
        hp.clickOnRegister()
        time.sleep(2)
        self.logger.info("***registrationPage******")
        rg = RegistrationPage(set_up)
        rg.set_Firstname("john")
        rg.set_lastname("milton")
        email = random_generator() + "@gamil.com"  #gh67j@gmail.com
        rg.set_email(email)
        rg.set_phonenumber("8765405678")
        rg.set_password("123456")
        rg.confirm_password("123456")
        self.logger.info("***clickin terms and conditions******")
        rg.agree_termsAndCon()
        self.logger.info("***clicking my account******")
        time.sleep(2)
        rg.clickOnContinue()
        exc_text="Your Account Has Been Created!"
        act_text=set_up.find_element(By.XPATH,"//h1[normalize-space()='Your Account Has Been Created!']").text
        if act_text==exc_text:
            assert True
        else:
            assert False

