from POM.login_page import LoginPage
from POM.reg_page import RegisterPage

import pytest

class TestLoginPage:
    def test_login(self, _driver):
        lp = LoginPage(_driver)
        lp.enter_email()
        lp.enter_password()
        lp.click_login()

class TestRegisterPage:
    def test_Register(self, Reg_driver):
        rp = RegisterPage(Reg_driver)
        rp.first_name()
        rp.last_name()
        rp.email()
        rp.password()
        rp.Conf_password()


