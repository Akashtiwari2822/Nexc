from selenium import webdriver
import pytest
# from selenium.webdriver.common.devtools.v107.cache_storage import delete_cache
from Config.config import Testdata
from clear_cache import clear as clear_cache

print('ak test')


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    clear_cache(dir=".")
    print("======================================= setup ========================================")
    print(request)

    if request.param == "chrome":
        web_driver = webdriver.Chrome()

    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=Testdata.FIREFOX_EXECUTABLE_PATH)
    web_driver.maximize_window()
    request.cls.driver = web_driver

    yield
    print("======================================= close setup ========================================")
    web_driver.close()
