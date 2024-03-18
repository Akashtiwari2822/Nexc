import csv
import pytest
from selenium import webdriver
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Config.config import Testdata
import configparser
from Config.credentialscheck import create_csv
from Config.updatesatus import *

filename = "/Config/config.ini"
print(filename)
config = configparser.ConfigParser()
config.read(filename)
try:
    config.add_section("LOGIN")
except configparser.DuplicateSectionError:
    print('error')
stored_exception = None
print("go making")
create_csv('./credentials/user_credentials.csv', ['username', 'password'])
print("done the making of file")


class TestLogin(BaseTest):

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_1", "TC1")])
    def test_signup_link_visible_RQ_ID_1_TC_1(self, requirement_id, testcase_id):
        self.loginpage = LoginPage(self.driver)
        flag = self.loginpage.is_signup_link_exits()
        if flag is True:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_2", "TC_2")])
    def test_login_page_title_RQ_ID_2_TC_2(self, requirement_id, testcase_id):
        self.loginpage = LoginPage(self.driver)
        titledata = self.loginpage.get_title(Testdata.TITLE)
        if titledata == Testdata.TITLE:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False
    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_2", "TC3")])
    def test_login_wrong_blank_RQ_ID_2_TC3(self, requirement_id, testcase_id):
        self.loginpage = LoginPage(self.driver)
        Testdatacsv = read_and_split_csv(requirement_id, testcase_id)
        message = self.loginpage.do_login_password_username_blank(Testdatacsv[0], Testdatacsv[1])
        # assert message == Testdata.LOGIN_BLANK_ALL_MESSAGE
        if message == Testdata.LOGIN_BLANK_ALL_MESSAGE:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_2", "TC4")])
    def test_login_username_blank_RQ_ID_2_TC4(self, requirement_id, testcase_id):
        self.loginpage = LoginPage(self.driver)
        Testdatacsv = read_and_split_csv(requirement_id, testcase_id)
        message = self.loginpage.do_login_password_username_blank('', Testdatacsv[1])
        # assert message == Testdata.LOGIN_BLANK_USERNAME_MESSAGE
        if message == Testdata.LOGIN_BLANK_USERNAME_MESSAGE:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_2", "TC5")])
    def test_login_password_blank_RQ_ID_2_TC5(self, requirement_id, testcase_id):
        self.loginpage = LoginPage(self.driver)
        Testdatacsv = read_and_split_csv(requirement_id, testcase_id)
        message = self.loginpage.do_login_password_username_blank(Testdatacsv[0], '')
        # assert message == Testdata.LOGIN_BLANK_USERNAME_MESSAGE
        if message == Testdata.LOGIN_BLANK_USERNAME_MESSAGE:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_2", "TC6")])
    def test_login_wrong_password_RQ_ID_2_TC7(self, requirement_id, testcase_id):
        self.loginpage = LoginPage(self.driver)
        Testdatacsv = read_and_split_csv(requirement_id, testcase_id)
        message = self.loginpage.do_login_password_wrong_username(Testdatacsv[0], Testdatacsv[1])
        # assert message == Testdata.LOGIN_WRONG_PASSWORD_MESSAGE
        if "Incorrect password entered" in message:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False
    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_2", "TC7")])
    def test_login_wrong_password_RQ_ID_2_TC7(self, requirement_id, testcase_id):
        self.loginpage = LoginPage(self.driver)
        message = self.loginpage.do_login_password_wrong_username(Testdata.USER_NAME, 'abc')
        # assert message == Testdata.LOGIN_WRONG_PASSWORD_MESSAGE
        if "Incorrect password entered" in message:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False
    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_2", "TC8")])
    def test_login_wrong_username_RQ_ID_2_TC_8(self, requirement_id, testcase_id):
        self.loginpage = LoginPage(self.driver)
        message = self.loginpage.do_login_password_username('akasht.sw', Testdata.PASSWORD)
        assert message == Testdata.LOGIN_WRONG_USERNAME_PASSWORD_MESSAGE
        if message == Testdata.LOGIN_WRONG_USERNAME_PASSWORD_MESSAGE:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False









    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_2", "TC2")])
    def test_login_check_RQ_ID_2_TC2(self, requirement_id, testcase_id):
        self.loginpage = LoginPage(self.driver)
        Testdatacsv = read_and_split_csv(requirement_id, testcase_id)
        message = self.loginpage.do_login_check(Testdatacsv[0], Testdatacsv[1])
        if message == Testdata.LOGIN_SUCESS_MESSAGE:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False
