import time
from Config.updatesatus import *
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import Testdata
import pytest

class Test_Home(BaseTest):

    @pytest.mark.parametrize("requirement_id, testcase_id", [("RQ_ID_9", "TC_9")])
    def test_menu_check_exit_RQ_ID_9_TC_9(self,requirement_id,testcase_id):
        self.loginPage = LoginPage(self.driver)
        Testdatacsv = read_and_split_csv(requirement_id, testcase_id)
        HomePage = self.loginPage.do_login(Testdatacsv[0], Testdatacsv[1])
        title = HomePage.Menuexitcheck(Testdatacsv[2])  # get_home_page_title(Testdata.TITLE)
        # assert title == Testdata.TITLE
        if title is True:
            update_status(requirement_id, testcase_id, "Pass")
            assert True
        else:
            update_status(requirement_id, testcase_id, "Fail")
            assert False
