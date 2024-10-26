import time

import pytest
from selenium import webdriver

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.Readproperties import Readconfig
from utilities.costomLogger import LogGen


class Test_login:
    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_login(self,set_up):
        self.logger.info("*****getting homepage******")
        hp = HomePage(set_up)
        time.sleep(2)
        hp.clickonMyaccount()
        hp.clickOnLogin()
        time.sleep(2)
        self.logger.info("*****getting loginpage**********")
        lp = LoginPage(set_up)
        time.sleep(3)
        self.logger.info("******entering username********")
        lp.enter_username(Readconfig.getUsermail())
        self.logger.info("*****entering password********")
        lp.enter_password(Readconfig.getpassword())
        self.logger.info("***clicking on login********")
        lp.clickonLogin()

        exc_url="https://tutorialsninja.com/demo/index.php?route=account/account"
        act_url=set_up.current_url

        if exc_url==act_url:
            assert True
            self.logger.info("****login is sucessfull*******")
        else:
            set_up.get_screenshot_as_file("C:\\Users\\KITS\\Documents\\New folder\\tut.png")
            set_up.save_screenshot("C:\\Users\\KITS\\PycharmProjects\\ecommerceproject\\Screenshots\\log.png")
            time.sleep(3)
            self.logger.info("******login is unsuccessful******")
            assert False

