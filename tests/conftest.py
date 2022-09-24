import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from . import config


def pytest_addoption(parser):
    parser.addoption("--baseurl",
                     action="store",
                     default="https://phptravels.net",
                     help="base URL for the application under test")


@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoption("--baseurl")
    # _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver')
    # if os.path.isfile(_chromedriver):
    driver_ = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # else:
    #     driver_ = webdriver.Chrome()

    def quit():
        driver_.quit()

    request.addfinalizer(quit)
    return driver_




