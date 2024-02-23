import time
from Pages.BasePage import BasePage
from Config.config import Testdata
from selenium.webdriver.common.by import By
from Pages.Homepage import HomePage


class LoginPage(BasePage):
    """ This is my by locators it is showing of the all input and other data  """
    EMAIL = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH,     "//button[@class='sc-ifAKCX ftiJlv']")
    # LOGIN_BUTTON = (By.XPATH, "//mat-horizontal-stepper/div[2]/div[1]/form/div[4]/button")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign Up")
    LOGIN_SUCESS_MESSAGE = (By.XPATH, "//p[@class='heading']")
    LOGIN_FAIL_MESSAGE = (By.XPATH, "//div[@class='sub-text']")
    LOGIN_ERROR_MESSAGE = (By.XPATH, "//span[@class='sc-hSdWYo eNOWSb']")
    SHOW_LOGOUT_BUTTON = (By.XPATH, "//div[@class='media']")
    LOGOUT_BUTTON = (By.XPATH, "//div[@class='sc-kgAjT jRpQlR selectable item ']")

    """ This is my constructor of the page class  """

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.driver.get(Testdata.BASE_URL)

    # this is my page action

    # this is get the page title
    def get_login_page_title(self, title):
        return self.get_title(title)

    # this is use to the signup test show or not
    def is_signup_link_exits(self):
        return self.is_visible(self.SIGNUP_LINK)

    # this showing the login button exits or not
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)

    def do_login_check(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        if self.is_visible(self.LOGIN_SUCESS_MESSAGE):
            val=self.get_element_text(self.LOGIN_SUCESS_MESSAGE)
            time.sleep(2)
            if self.is_visible(self.SHOW_LOGOUT_BUTTON):
                self.do_click(self.SHOW_LOGOUT_BUTTON)
            time.sleep(2)
            if self.is_visible(self.LOGOUT_BUTTON):
                self.do_click(self.LOGOUT_BUTTON)
            return val
        else:
            return 'fail'

    def do_login_password_username(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        if self.is_visible(self.LOGIN_ERROR_MESSAGE):
            return self.get_element_text(self.LOGIN_ERROR_MESSAGE)

    def do_login_password_wrong_username(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        if self.is_visible(self.LOGIN_FAIL_MESSAGE):
            return self.get_element_text(self.LOGIN_FAIL_MESSAGE)

    def do_login_password_username_blank(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        if self.is_visible(self.LOGIN_ERROR_MESSAGE):
            return self.get_element_text(self.LOGIN_ERROR_MESSAGE)
