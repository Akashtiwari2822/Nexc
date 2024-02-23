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

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_1", "TC_1")])
    def test_signup_link_visible_RQ_ID_1_TC_1(self,requirement_id,testcase_id):
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

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_3", "TC_3")])
    def test_login_wrong_username_RQ_ID_3_TC_3(self,requirement_id,testcase_id):
        self.loginpage = LoginPage(self.driver)
        message = self.loginpage.do_login_password_username('akasht.sw', Testdata.PASSWORD)
        assert message == Testdata.LOGIN_WRONG_USERNAME_PASSWORD_MESSAGE
        if message == Testdata.LOGIN_WRONG_USERNAME_PASSWORD_MESSAGE:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_4", "TC_4")])
    def test_login_wrong_password_RQ_ID_4_TC_4(self,requirement_id,testcase_id):
        self.loginpage = LoginPage(self.driver)
        message = self.loginpage.do_login_password_wrong_username(Testdata.USER_NAME, 'abc')
        # assert message == Testdata.LOGIN_WRONG_PASSWORD_MESSAGE
        if "Incorrect password entered" in message:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_5", "TC_5")])
    def test_login_wrong_blank_RQ_ID_5_TC_4(self,requirement_id,testcase_id):
        self.loginpage = LoginPage(self.driver)
        message = self.loginpage.do_login_password_username_blank('', '')
        # assert message == Testdata.LOGIN_BLANK_ALL_MESSAGE
        if message == Testdata.LOGIN_BLANK_ALL_MESSAGE:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_6", "TC_6")])
    def test_login_username_blank_RQ_ID_6_TC_5(self,requirement_id,testcase_id):
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

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_7", "TC_7")])
    def test_login_password_blank_RQ_ID_7_TC_7(self,requirement_id,testcase_id):
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

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_8", "TC_8")])
    def test_login_check_RQ_ID_8_TC_8(self,requirement_id,testcase_id):
        self.loginpage = LoginPage(self.driver)
        Testdatacsv=read_and_split_csv(requirement_id,testcase_id)
        message = self.loginpage.do_login_check(Testdatacsv[0], Testdatacsv[1])
        # assert message == Testdata.LOGIN_SUCESS_MESSAGE
        if message == Testdata.LOGIN_SUCESS_MESSAGE:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False
