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
        title = HomePage.check_playlist_onair_load_button_disable(Testdatacsv[2],
                                                                  Testdatacsv[3])  # get_home_page_title(Testdata.TITLE)
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
        title = HomePage.check_playlist_onair_append_button_disable(Testdatacsv[2], Testdatacsv[
            3])  # get_home_page_title(Testdata.TITLE)
        if title is True:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_15", "TC_15")])
    def test_appen_popup_open_RQ_ID_15_TC_15(self, requirement_id, testcase_id):
        self.loginPage = LoginPage(self.driver)
        Testdatacsv = read_and_split_csv(requirement_id, testcase_id)
        HomePage = self.loginPage.do_login(Testdatacsv[0], Testdatacsv[1])
        title = HomePage.check_load_append_popup_showing(Testdatacsv[2])  # get_home_page_title(Testdata.TITLE)
        if title is True:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_16", "TC_16")])
    def test_appen_playlist_delete_option_RQ_ID_16_TC_16(self, requirement_id, testcase_id):
        self.loginPage = LoginPage(self.driver)
        Testdatacsv = read_and_split_csv(requirement_id, testcase_id)
        HomePage = self.loginPage.do_login(Testdatacsv[0], Testdatacsv[1])
        title = HomePage.check_append_delete_optionshowing(Testdatacsv[2],Testdatacsv[3],Testdatacsv[4])  # get_home_page_title(Testdata.TITLE)
        if title is True:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_17", "TC_17")])
    def test_manage_playlist_delete_RQ_ID_17_TC_17(self, requirement_id, testcase_id):
        self.loginPage = LoginPage(self.driver)
        Testdatacsv = read_and_split_csv(requirement_id, testcase_id)
        HomePage = self.loginPage.do_login(Testdatacsv[0], Testdatacsv[1])
        title = HomePage.check_mamange_playlist(Testdatacsv[2],Testdatacsv[3])  # get_home_page_title(Testdata.TITLE)
        if title is True:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_18", "TC_18")])
    def test_verify_the_edit_allmenu_show_RQ_ID_18_TC_18(self, requirement_id, testcase_id):
        self.loginPage = LoginPage(self.driver)
        Testdatacsv = read_and_split_csv(requirement_id, testcase_id)
        HomePage = self.loginPage.do_login(Testdatacsv[0], Testdatacsv[1])
        title = HomePage.editmenu_verify(Testdatacsv[2], Testdatacsv[3],Testdatacsv,[4])  # get_home_page_title(Testdata.TITLE)
        if title is True:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False
