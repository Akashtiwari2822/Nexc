import time

from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import Testdata


class Test_Home(BaseTest):

    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        HomePage = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        title = HomePage.get_home_page_title(Testdata.TITLE)  # get_home_page_title(Testdata.TITLE)
        assert title == Testdata.TITLE

    def test_home_to_move_cloudx(self):
        time.sleep(3)
        self.loginPage = LoginPage(self.driver)
        HomePage = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        header = HomePage.contido_to_cloudx()
        assert header == Testdata.PLAYOUTPAGE

    def test_home_to_move_recaster(self):
        self.loginPage = LoginPage(self.driver)
        HomePage = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        header = HomePage.contido_to_recaster(Testdata.RECASTERPAGE)
        assert header == Testdata.RECASTERPAGE

    def test_cloudx_to_recaster(self):
        self.loginPage = LoginPage(self.driver)
        HomePage = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        header = HomePage.cloudx_to_recaster(Testdata.RECASTERPAGE)
        assert header == Testdata.RECASTERPAGE

    def test_recaster_to_cloudx(self):
        self.loginPage = LoginPage(self.driver)
        HomePage = self.loginPage.do_login(Testdata.USER_NAME, Testdata.PASSWORD)
        header = HomePage.recaster_to_cloudx()
        assert header == Testdata.PLAYOUTPAGE
