'''
POM : Page Object Model design pattern to write business logic

'''

from data import reading_objects
# from data import reading_objects
from selenium import webdriver
from Library.sel_wrapper import SeleniumWrapper
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
# driver.get("https://demowebshop.tricentis.com/login")
# driver.maximize_window()

login_objects = reading_objects.read_locator()



class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.sel_wrapper = SeleniumWrapper(driver)

    def enter_email(self):
        # driver.find_element(*login_objects['txt_email']).send_keys("VKam@gmail.com")
        self.sel_wrapper.enter_text(login_objects['txt_email'], 'VKam@gmail.com')

    def enter_password(self):
        # driver.find_element(*login_objects['txt_password']).send_keys("123456789")
        self.sel_wrapper.enter_text(login_objects['txt_password'], "123456789")

    def click_login(self):
        # driver.find_element(*login_objects['btn_login']).click()
        self.sel_wrapper.click_element(login_objects['btn_login'])

# lp = LoginPage(driver)
# lp.enter_email()
# lp.enter_password()
# lp.click_login()





