import pytest
import time
import selenium
import csv
import pytest
from selenium import webdriver
from clear_cache import clear as clear_cache
from Config.config import Testdata
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Config.config import Testdata
import configparser
from Config.credentialscheck import *
from Config.updatesatus import *
import subprocess
from Config.HomePageXpath import sourcepath
import logging
logging.basicConfig(filename='Logfile.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def run_tests(name):
    # Run pytest with desired command line arguments
    time.sleep(1)
    if name == 'all':
        
        pytest.main(["-v", "testing/"])
    elif name == 'page':
         requirement_id = input("Enter the Page Name: ")
         pytest.main(["-v", f"testing/test_{name}.py"])
    elif name == 'other':
          pagenme= input("Enter the Page name : ")
          casename = input("Enter the case name: ")
          requirement_id = input("Enter the requirement ID: ")
          testcase_id = input("Enter the testcase ID: ")
          args = ["-v", "-k", f"{casename}_{requirement_id}_{testcase_id}", "testing/test_functional.py"]
          result = pytest.main(args)


if __name__ == "__main__":
    time.sleep(1)
    try:
        # pytest.main(["-v", "testing/"])
         while True:
             print('''enter the page name test name requirment id and testcase id if test all case then enter all single command testcase run enter 
                   

                   type of command :- all 
                   Page
                   other
                   ''')
             name = input("Enter your page name run: ")
             run_tests(name)
    except Exception as e:
            print(f"Exception occurred: {e}")
            logging.error('This is an error message: {e}')
            time.sleep(50)
    # pytest.main(["-v", "./testing/ --csv=reports/test_report.csv --html=reports/test_report.html"])
    # pytest.main(["-v", "./testing/", "--csv=reports/test_report.csv", "--html=reports/test_report.html"])
    # pytest.main(["-v", "--csv=reports/test_report.csv", "--html=reports/test_report.html", "./testing/test_functional.py"])
    # args = ["-v", "./testing/test_functional.py", "--csv=reports/test_report.csv", "--html=reports/test_report.html"]
    # pytest.main(args.split())
    # command = "pytest ./testing/test_functional.py --csv=reports/test_report.csv --html=reports/test_report.html"
    # subprocess.run(command, shell=True)
    time.sleep(50)
