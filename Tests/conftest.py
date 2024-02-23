from selenium import webdriver
import pytest
# from selenium.webdriver.common.devtools.v107.cache_storage import delete_cache
from Config.config import Testdata
from clear_cache import clear as clear_cache
from selenium.webdriver.chrome.options import Options
print('ak test')




# @pytest.fixture(params=["firefox","chrome"], scope='class')
@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    clear_cache(dir=".")
    print("======================================= setup ========================================")
    print(request)
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    if request.param == "chrome":

        web_driver = webdriver.Chrome()
        # web_driver = webdriver.Chrome(options=chrome_options)

        # web_driver.addArguments("--headless")

    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    web_driver.maximize_window()
    # web_driver.addArguments("--headless")
    request.cls.driver = web_driver

    yield
    print("======================================= close setup ========================================")
    web_driver.close()

