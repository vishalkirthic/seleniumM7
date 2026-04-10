import pytest
from selenium import webdriver


@pytest.fixture()
def _driver():

    opts = webdriver.ChromeOptions()

    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=opts)

    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/login")
    yield driver

    driver.quit()
    
@pytest.fixture()
def Reg_driver():

    opts = webdriver.ChromeOptions()

    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=opts)
    
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/register")
    yield driver

    driver.quit()

"""
1. project is a combination of data driven approach and unit testing framework
2. store the data in excel, and read from it
3. write the business logic in POM
4. write the generic functions
5. test cases 
6. share the common codes, conftest
"""





