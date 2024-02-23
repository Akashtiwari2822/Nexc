import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.HomePageXpath import sourcepath


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        # return self.get_title(title)
        if self.is_visible(sourcepath.LOGIN_SUCESS_MESSAGE):
            val = self.get_title(title)
            time.sleep(2)
            if self.is_visible(sourcepath.SHOW_LOGOUT_BUTTON):
                self.do_click(sourcepath.SHOW_LOGOUT_BUTTON)
            time.sleep(2)
            if self.is_visible(sourcepath.LOGOUT_BUTTON):
                self.do_click(sourcepath.LOGOUT_BUTTON)
            return val

    def contido_to_cloudx(self):
        self.do_hover_and_click(sourcepath.HOVER_BUTTON, sourcepath.CLOUDX_BUUTON)
        time.sleep(2)
        if self.is_visible(sourcepath.PLAYOUTDASHBOARD):
            val = self.get_element_text(sourcepath.PLAYOUTDASHBOARD)
            time.sleep(2)
            if self.is_visible(sourcepath.CLOUDX_SHOW_LOGOUT_BUTTON):
                self.do_click(sourcepath.CLOUDX_SHOW_LOGOUT_BUTTON)
            time.sleep(2)
            if self.is_visible(sourcepath.CLOUDX_LOGOUT_BUTTON):
                self.do_click(sourcepath.CLOUDX_LOGOUT_BUTTON)
            return val
        return self.get_element_text(sourcepath.PLAYOUTDASHBOARD)

    def contido_to_recaster(self, title):
        self.do_hover_and_click(self.HOVER_BUTTON, sourcepath.RECASTERPAGE)
        time.sleep(2)
        val = self.get_title(title)
        # self.do_click(self.RECASTER_SHOW_LOGOUT_BUTTON)
        time.sleep(5)
        self.do_click(sourcepath.RECASTER_LOGOUT_BUTTON)

        return val

    def cloudx_to_recaster(self, title):
        self.do_hover_and_click(sourcepath.HOVER_BUTTON, sourcepath.CLOUDX_BUUTON)
        time.sleep(2)
        self.do_hover_and_click(sourcepath.CLOUDX_HOVER_BUTTON, sourcepath.CLOUDX_TO_RECASTER_BUTTON)
        val = self.get_title(title)
        # self.do_click(self.RECASTER_SHOW_LOGOUT_BUTTON)
        self.do_click(self.RECASTER_LOGOUT_BUTTON)

        return val

    def recaster_to_cloudx(self):
        self.do_hover_and_click(sourcepath.HOVER_BUTTON, sourcepath.RECASTERPAGE)
        time.sleep(2)
        self.do_hover_and_click(sourcepath.RECASTER_HOVER_BUTTON, sourcepath.RECASTERPAGE_TO_CLOUDX)
        time.sleep(1)
        if self.is_visible(sourcepath.PLAYOUTDASHBOARD):
            val = self.get_element_text(sourcepath.PLAYOUTDASHBOARD)
            time.sleep(2)
            if self.is_visible(sourcepath.CLOUDX_SHOW_LOGOUT_BUTTON):
                self.do_click(sourcepath.CLOUDX_SHOW_LOGOUT_BUTTON)
            time.sleep(2)
            if self.is_visible(sourcepath.CLOUDX_LOGOUT_BUTTON):
                self.do_click(sourcepath.CLOUDX_LOGOUT_BUTTON)
            return val
        return self.get_element_text(sourcepath.PLAYOUTDASHBOARD)

    def Menuexitcheck(self, channelname):
        val = '//div[@data-channel="' + channelname + '"]'
        carname = (By.XPATH, val)
        self.do_hover_and_click(sourcepath.HOVER_BUTTON, sourcepath.CLOUDX_BUUTON)
        time.sleep(1)
        self.do_click(carname)
        if self.is_visible(sourcepath.Filemenu) == self.is_visible(sourcepath.TOOLSMENU) == self.is_visible(
                sourcepath.PLAYOUTMENU) == self.is_visible(sourcepath.EDITMENU) == self.is_visible(sourcepath.VIEWMENU):
            return True
        else:
            return False

    def check_load_playlist(self, channelname):
        val = '//div[@data-channel="' + channelname + '"]'
        carname = (By.XPATH, val)
        self.do_hover_and_click(sourcepath.HOVER_BUTTON, sourcepath.CLOUDX_BUUTON)
        time.sleep(1)
        self.do_click(carname)
        time.sleep(1)
        self.do_hover(sourcepath.Filemenu)
        self.do_click(sourcepath.LOADPLAYLISTBUTTON)
        if self.is_visible(sourcepath.LOADPLAYLISTBUTTONTEXT) is True:
            self.do_click(sourcepath.BACKBUTTON)
            self.do_click(sourcepath.CLOUDX_SHOW_LOGOUT_BUTTON)
            self.do_click(sourcepath.CLOUDX_LOGOUT_BUTTON)
            return True
        else:
            return False

    def check_load_playlist_count(self, channelname):
        val = '//div[@data-channel="' + channelname + '"]'
        carname = (By.XPATH, val)
        self.do_hover_and_click(sourcepath.HOVER_BUTTON, sourcepath.CLOUDX_BUUTON)
        time.sleep(1)
        self.do_click(carname)
        time.sleep(1)
        self.do_hover(sourcepath.Filemenu)
        self.do_click(sourcepath.LOADPLAYLISTBUTTON)
        time.sleep(1)
        data = self.count_data(sourcepath.COUNTPLAYLIST)
        print(data)
        datanew = self.get_element_text(sourcepath.NUMBEROFCOUNT)
        data = "Result : " + str(data)
        if data == datanew:
            self.do_click(sourcepath.BACKBUTTON)
            time.sleep(2)
            self.do_click(sourcepath.CLOUDX_SHOW_LOGOUT_BUTTON)
            time.sleep(2)
            self.do_click(sourcepath.CLOUDX_LOGOUT_BUTTON)
            time.sleep(2)
            return True
        else:
            return False

    def check_playlist_uploadbutton_showing_dashboard(self, channelname):
        val = '//div[@data-channel="' + channelname + '"]'
        carname = (By.XPATH, val)
        self.do_hover_and_click(sourcepath.HOVER_BUTTON, sourcepath.CLOUDX_BUUTON)
        time.sleep(1)
        self.do_click(carname)
        if self.is_visible(sourcepath.CHECKACCESS) is True:
            self.do_click(sourcepath.CHECKACCESS)
        if self.is_visible(sourcepath.REQUESTADMIN) is True:
            self.do_click(sourcepath.REQUESTADMIN)
            time.sleep(5)
        if self.is_enabled(sourcepath.STOPBUTTON) is True:
            if self.is_visible(sourcepath.REQUESTADMIN):
                self.do_click(sourcepath.REQUESTADMIN)
                time.sleep(5)
            self.do_click(sourcepath.STOPBUTTON)
            self.do_click(sourcepath.STOPYES)
        time.sleep(3)
        self.do_hover(sourcepath.EDITBUTTON)
        time.sleep(1)
        self.do_click(sourcepath.DELETEALLBUTTON)
        time.sleep(1)
        if self.is_visible(sourcepath.STOPYES) is True:
            self.do_click(sourcepath.STOPYES)
        time.sleep(2)
        self.do_hover(sourcepath.Filemenu)
        self.do_click(sourcepath.LOADPLAYLISTBUTTON)
        time.sleep(3)
        data = self.get_element_text(sourcepath.TEXTNOTPLAYLISTEXIT)
        if data == "No playlist available!":
            time.sleep(3)
            self.do_click(sourcepath.BACKBUTTON)
            time.sleep(5)
            self.do_click(sourcepath.CLOUDX_SHOW_LOGOUT_BUTTON)
            time.sleep(2)
            self.do_click(sourcepath.CLOUDX_LOGOUT_BUTTON)
            time.sleep(2)
            return True
        else:
            return False

    def getacess(self):
        if self.is_visible(sourcepath.CHECKACCESS) is True:
            self.do_click(sourcepath.CHECKACCESS)
        if self.is_visible(sourcepath.CHECKACCESS) is True:
            self.do_click(sourcepath.CHECKACCESS)
        if self.is_visible(sourcepath.REQUESTADMIN) is True:
            self.do_click(sourcepath.REQUESTADMIN)
            time.sleep(5)

    def check_playlist_onair_load_button_disable(self, channelname, playlistname):
        val = '//div[@data-channel="' + channelname + '"]'
        carname = (By.XPATH, val)
        self.do_hover_and_click(sourcepath.HOVER_BUTTON, sourcepath.CLOUDX_BUUTON)
        hoverbtn = "//div[@title='" + playlistname + "']"
        hoverbtn = (By.XPATH, hoverbtn)
        time.sleep(1)
        self.do_click(carname)
        self.getacess()
        if self.check_enginerun() == "yes":
            self.do_hover(sourcepath.Filemenu)
            self.do_click(sourcepath.LOADPLAYLISTBUTTON)
            self.do_hover(hoverbtn)
            valnew = "//div[contains(@title,'" + playlistname + "')]//div[contains(@class,'plListAction w3-animate-zoom')]//div//button[contains(@class,'btnDisabled')][normalize-space()='Load']"
            # cxpathn = (By.XPATH, cxpath)
            cxpathn = (By.XPATH, valnew)
            if self.is_enabled(cxpathn) is True:
                self.do_click(sourcepath.BACKBUTTON)
                time.sleep(2)
                self.do_click(sourcepath.CLOUDX_SHOW_LOGOUT_BUTTON)
                time.sleep(2)
                self.do_click(sourcepath.CLOUDX_LOGOUT_BUTTON)
                time.sleep(2)
                return True
            else:
                return False
        else:
            self.do_hover(sourcepath.Filemenu)
            self.do_click(sourcepath.LOADPLAYLISTBUTTON)
            time.sleep(5)
            self.do_click(sourcepath.STARTPLAY)
            self.do_click(sourcepath.STOPYES)
            time.sleep(5)
            self.do_hover(sourcepath.Filemenu)
            self.do_click(sourcepath.LOADPLAYLISTBUTTON)
            self.do_hover(hoverbtn)
            valnew = "//div[contains(@title,'" + playlistname + "')]//div[contains(@class,'plListAction w3-animate-zoom')]//div//button[contains(@class,'btnDisabled')][normalize-space()='Load']"
            # cxpathn = (By.XPATH, cxpath)
            cxpathn = (By.XPATH, valnew)
            if self.is_enabled(cxpathn) is True:
                self.do_click(sourcepath.BACKBUTTON)
                time.sleep(2)
                self.do_click(sourcepath.CLOUDX_SHOW_LOGOUT_BUTTON)
                time.sleep(2)
                self.do_click(sourcepath.CLOUDX_LOGOUT_BUTTON)
                time.sleep(2)
                return True
            else:
                return False

    def check_playlist_onair_append_button_disable(self, channelname, playlistname):
        val = '//div[@data-channel="' + channelname + '"]'
        carname = (By.XPATH, val)
        self.do_hover_and_click(sourcepath.HOVER_BUTTON, sourcepath.CLOUDX_BUUTON)
        time.sleep(1)
        self.do_click(carname)
        if self.is_visible(sourcepath.CHECKACCESS) is True:
            self.do_click(sourcepath.CHECKACCESS)
        if self.is_visible(sourcepath.REQUESTADMIN) is True:
            self.do_click(sourcepath.REQUESTADMIN)
            time.sleep(5)
        hoverbtn = "//div[@title='" + playlistname + "']"
        hoverbtn = (By.XPATH, hoverbtn)
        if self.is_enabled(sourcepath.STOPBUTTON) is True:
            valnew = "//div[contains(@title,'" + playlistname + "')]//div[contains(@class,'plListAction w3-animate-zoom')]//div//button[contains(@class,'btnDisabled')][normalize-space()='Append']"
            # cxpathn = (By.XPATH, cxpath)
            cxpathn = (By.XPATH, valnew)
            time.sleep(4)
            self.do_click(sourcepath.STOPBUTTON)
            self.do_click(sourcepath.STOPYES)
            time.sleep(4)
            self.do_hover(sourcepath.EDITBUTTON)
            time.sleep(1)
            self.do_click(sourcepath.DELETEALLBUTTON)
            self.do_click(sourcepath.STOPYES)
            self.do_hover(sourcepath.Filemenu)
            self.do_click(sourcepath.LOADPLAYLISTBUTTON)
            self.do_hover(hoverbtn)
            if self.is_enabled(cxpathn) is False:
                self.do_click(sourcepath.BACKBUTTON)
                time.sleep(2)
                self.do_click(sourcepath.CLOUDX_SHOW_LOGOUT_BUTTON)
                time.sleep(2)
                self.do_click(sourcepath.CLOUDX_LOGOUT_BUTTON)
                time.sleep(2)
                return True
            else:
                return False
        else:
            valnew = "//div[@title='" + playlistname + "']//div//div//button[contains(text(),'Load')]"
            cxpathn = (By.XPATH, valnew)
            # self.do_click(self.STOPBUTTON)
            # self.do_click(self.STOPYES)
            # time.sleep(2)
            self.do_hover(sourcepath.EDITBUTTON)
            time.sleep(1)
            self.do_click(sourcepath.DELETEALLBUTTON)
            self.do_click(sourcepath.STOPYES)
            self.do_hover(sourcepath.Filemenu)
            self.do_click(sourcepath.LOADPLAYLISTBUTTON)
            # self.do_click(cxpathn)
            time.sleep(2)
            self.do_hover(sourcepath.Filemenu)
            self.do_click(sourcepath.LOADPLAYLISTBUTTON)
            self.do_hover(hoverbtn)
            if self.is_visible(cxpathn) is True:
                self.do_click(sourcepath.BACKBUTTON)
                time.sleep(2)
                self.do_click(sourcepath.CLOUDX_SHOW_LOGOUT_BUTTON)
                time.sleep(2)
                self.do_click(sourcepath.CLOUDX_LOGOUT_BUTTON)
                time.sleep(2)
                return True
            else:
                return False

    def check_load_append_popup_showing(self, channelname):
        # self.do_click(sourcepath)
        val = '//div[@data-channel="' + channelname + '"]'
        carname = (By.XPATH, val)
        self.do_hover_and_click(sourcepath.HOVER_BUTTON, sourcepath.CLOUDX_BUUTON)
        time.sleep(1)
        self.do_click(carname)
        self.getacess()
        time.sleep(2)
        self.do_click(sourcepath.Filemenu)
        time.sleep(1)
        self.do_click(sourcepath.APPENBUTTON)
        if self.get_element_text(sourcepath.APPENPOPUP) == "Load Playlist":
            self.do_click(sourcepath.BACKBUTTON)
            time.sleep(2)
            self.do_click(sourcepath.CLOUDX_SHOW_LOGOUT_BUTTON)
            time.sleep(2)
            self.do_click(sourcepath.CLOUDX_LOGOUT_BUTTON)
            time.sleep(2)
            return True
        else:
            return False

    def go_to_in_cloudx_channel_screen(self, channelname):
        val = '//div[@data-channel="' + channelname + '"]'
        carname = (By.XPATH, val)
        self.do_hover_and_click(sourcepath.HOVER_BUTTON, sourcepath.CLOUDX_BUUTON)
        time.sleep(1)
        self.do_click(carname)
        self.getacess()

    def logout_session(self):
        self.do_click(sourcepath.BACKBUTTON)
        time.sleep(2)
        self.do_click(sourcepath.CLOUDX_SHOW_LOGOUT_BUTTON)
        time.sleep(2)
        self.do_click(sourcepath.CLOUDX_LOGOUT_BUTTON)
        time.sleep(2)

    def check_enginerun(self):
        if self.is_enabled(sourcepath.STARTPLAY) is True:
            return "no"
        else:
            return "yes"

    def appen_playlist(self):
        self.do_click(sourcepath.Filemenu)
        time.sleep(1)
        self.do_click(sourcepath.APPENPOPUP)

    def Appen_playlist_check(self, channelname):
        self.go_to_in_cloudx_channel_screen(channelname)
        if self.check_enginerun() == "yes":
            self.appen_playlist()
