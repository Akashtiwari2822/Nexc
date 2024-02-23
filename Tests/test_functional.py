import time
from Config.updatesatus import *
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import Testdata
import pytest


class Test_Home(BaseTest):

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_10", "TC_10")])
    def test_locad_playlist_section_exit_RQ_ID_10_TC_10(self, requirement_id, testcase_id):
        self.loginPage = LoginPage(self.driver)
        Testdatacsv = read_and_split_csv(requirement_id, testcase_id)
        HomePage = self.loginPage.do_login(Testdatacsv[0], Testdatacsv[1])
        title = HomePage.check_load_playlist(Testdatacsv[2])  # get_home_page_title(Testdata.TITLE)
        # assert title == Testdata.TITLE
        if title is True:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False


    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_11", "TC_11")])
    def test_load_playlist_count_match_RQ_ID_11_TC_11(self, requirement_id, testcase_id):
        self.loginPage = LoginPage(self.driver)
        Testdatacsv = read_and_split_csv(requirement_id, testcase_id)
        HomePage = self.loginPage.do_login(Testdatacsv[0], Testdatacsv[1])
        title = HomePage.check_load_playlist_count(Testdatacsv[2])  # get_home_page_title(Testdata.TITLE)
        # assert title == Testdata.TITLE
        if title is True:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_12", "TC_12")])
    def test_load_Upload_button_showing_RQ_ID_12_TC_12(self, requirement_id, testcase_id):
        self.loginPage = LoginPage(self.driver)
        Testdatacsv = read_and_split_csv(requirement_id, testcase_id)
        HomePage = self.loginPage.do_login(Testdatacsv[0], Testdatacsv[1])
        title = HomePage.check_playlist_uploadbutton_showing_dashboard(Testdatacsv[2])  # get_home_page_title(Testdata.TITLE)
        if title is True:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False
