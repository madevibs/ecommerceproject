import random
import string
import time

import pytest
from selenium import webdriver

from utilities.Readproperties import Readconfig
from utilities.costomLogger import LogGen

logger = LogGen.loggen()


@pytest.yield_fixture(params=["chrome"])
def set_up(request):
    logger.info("********launching the browser**********")
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options)
    elif request.param == "edge":
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options)
    elif request.param== "firefox":
        driver = webdriver.Firefox()

    logger.info("********launching the applicaton*********")
    driver.get(Readconfig.getApplicationUrl())
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    time.sleep(2)
    logger.info("*******closing the browser***********")
    driver.close()
    driver.quit()

def random_generator(size=5,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))






