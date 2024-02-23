from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui
import pytest
from selenium.webdriver.common.action_chains import ActionChains
import time

""" This page is all pages comman page   """
""" it contain all the generic methods and utilites for all pages   """


class BasePage:
    # __int is behave a constructure function

    def __init__(self, driver):
        self.driver = driver

    def do_hover(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def do_hover_and_click(self, hover_locator, click_locator):
        try:
            hover_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(hover_locator))
            action = ActionChains(self.driver)
            action.move_to_element(hover_element).perform()

            # Add a small delay (adjust the sleep duration as needed)
            time.sleep(1)

            # Perform the click after the hover on a different element
            click_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(click_locator))
            click_element.click()
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def do_click(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def do_clear(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def do_click_force(self, by_locator):
        self.driver.execute_script("arguments[0].click();",
                                   WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)))

    def do_send_keys(self, by_locator, text):
        try: 
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def get_element_text(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return element.text
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def get_element_text_new(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return element.get_attribute
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def is_enabled(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
            return element.is_enabled()
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False

    def is_visible(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return True
        except:
            return False
        # return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_currenturl(self, currenturl):
        WebDriverWait(self.driver, 10).until(EC.url_changes(currenturl))
        return self.driver.currenturl

    def do_upload(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).click()
        pyautogui.write(text)
        pyautogui.press('enter')

    def count_data(self, path):
        try:
            elements = self.driver.find_elements(By.XPATH, path)
            time.sleep(1)
            class_count = len(elements)
            # data=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(path)).find_element()
            # class_count = len(data)
            return class_count
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False
