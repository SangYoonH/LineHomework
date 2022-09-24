from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests import config

class LoginPage(BasePage):
    _username_input = {"by": By.NAME, "value": "email"}
    _password_input = {"by": By.NAME, "value": "password"}
    _submit_button = {"by": By.CSS_SELECTOR, "value": "button"}
    _success_message = {"value": "Dashboard"}
    # _failure_message = {"by": By.CSS_SELECTOR, "value": ".flash.error"}
    _login_title = {"value": "Login"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("/api/admin")
        assert self._get_title(self._login_title)

    def with_(self, username, password):
        self._type(self._username_input, username)
        self._type(self._password_input, password)
        self._click(self._submit_button)

    def dashboard_page_present(self):
        return self._get_title(self._success_message, config.login_success_timeout)
    #
    # def failure_message_present(self):
    #     return self._is_displayed(self._failure_message, 1)

    # def test_invalid_credentials(self, login):
    #     login.with_("tomsmith", "bad password")
    #     assert login.failure_message_present()