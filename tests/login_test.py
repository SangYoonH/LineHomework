import pytest
from pages import login_page
from . import config


@pytest.fixture
def login(driver):
    return login_page.LoginPage(driver)


@pytest.mark.order(1)
def test_valid_credentials(login):
    login.with_(config.valid_username, config.valid_password)
    assert login.login_success_check()
