import pytest
from pages import login_page
from . import config


@pytest.fixture
def login(driver):
    return login_page.LoginPage(driver)


def test_valid_credentials(login):
    login.with_(config.valid_email, config.valid_password)
    assert login.login_success_check()
    assert login.goto_customers_page()




#
#
# def test_invalid_credentials(login):
#     login.with_("admin@phptravels.com", "bad password")
#     assert login.failure_message_present()
