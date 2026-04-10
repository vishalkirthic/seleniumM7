from Library.gen_reg import reg_wrapper
from selenium import webdriver
from data import reading_reg
from data import reading_objects
import time

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=opts)
# driver.get("https://demowebshop.tricentis.com/register")
# driver.maximize_window()

reg_objects = reading_objects.read_locator("reg_details")
# print(reg_objects)

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.gen_reg = reg_wrapper(driver)

    def first_name(self):
        # driver.find_element(*reg_objects['txt_fname']).send_keys('Vishal')
        self.gen_reg.enter_text(reg_objects['txt_fname'], 'Vishal')

    def last_name(self):
        # driver.find_element(*reg_objects['txt_lname']).send_keys('A M')
        self.gen_reg.enter_text(reg_objects['txt_lname'], 'A M')

    def email(self):
        # driver.find_element(*reg_objects['txt_email']).send_keys('VKam@gmail.com')
        self.gen_reg.enter_text(reg_objects['txt_email'], 'VKam@gmail.com')

    def password(self):
        # driver.find_element(*reg_objects['txt_pwd']).send_keys('12345678')
        self.gen_reg.enter_text(reg_objects['txt_pwd'], '12345678')

    def Conf_password(self):
        # driver.find_element(*reg_objects['txt_confpwd']).send_keys('12345678')
        self.gen_reg.enter_text(reg_objects['txt_confpwd'], '12345678')

    def reg_button(self):
        # driver.find_element(*reg_objects['btn_reg']).click()
        self.gen_reg.click_element(reg_objects['btn_reg'])

    # def call_methods(self):
    #     methods = inspect.getmembers(self, predicate=inspect.ismethod)
    #     for name, method in methods:
    #         if name != 'call_methods' and not name.startswith('__'):
    #             method()

# Reg = RegisterPage(driver)
# Reg.first_name()
# Reg.last_name()
# Reg.email()
# Reg.password()
# Reg.Conf_password()
# time.sleep(10)
