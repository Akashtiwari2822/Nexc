import time
from Config.updatesatus import *
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import Testdata
import pytest


class Test_Home(BaseTest):


    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_13", "TC_13")])
    def test_load_button_disable_RQ_ID_13_TC_13(self, requirement_id, testcase_id):
        self.loginPage = LoginPage(self.driver)
        Testdatacsv = read_and_split_csv(requirement_id, testcase_id)
        HomePage = self.loginPage.do_login(Testdatacsv[0], Testdatacsv[1])
        title = HomePage.check_playlist_onair_load_button_disable(Testdatacsv[2],Testdatacsv[3])  # get_home_page_title(Testdata.TITLE)
        if title is True:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_14", "TC_14")])
    def test_append_button_disable_RQ_ID_14_TC_14(self, requirement_id, testcase_id):
        self.loginPage = LoginPage(self.driver)
        Testdatacsv = read_and_split_csv(requirement_id, testcase_id)
        HomePage = self.loginPage.do_login(Testdatacsv[0], Testdatacsv[1])
        title = HomePage.check_playlist_onair_append_button_disable(Testdatacsv[2],Testdatacsv[3])  # get_home_page_title(Testdata.TITLE)
        if title is True:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False
