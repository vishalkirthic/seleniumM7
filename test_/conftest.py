# to share the common codes
from selenium import webdriver
import pytest
import time

@pytest.fixture()
def _driver():
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=opts)
    driver.get("https://demowebshop.tricentis.com/login")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def Reg_driver():
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=opts)
    driver.get("https://demowebshop.tricentis.com/register")
    driver.maximize_window()
    yield driver
    time.sleep(5)
    driver.quit()

"""
1. project is a combination of data driven approach and unit testing framework
2. store the data in excel, and read from it
3. write the business logic in POM
4. write the generic functions
5. test cases 
6. share the common codes, conftest
"""





