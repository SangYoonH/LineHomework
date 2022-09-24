# from selenium.webdriver.common.by import By
# from pages.base_page import BasePage
# from tests import config
#
#
# class DashboardPage(BasePage):
#     _customers_page = {"by": By.CSS_SELECTOR,
#                        "value": "a[href*='https://phptravels.net/api/admin/accounts/customers/']"}
#     _menu_button = {"by": By.ID, "value": "drawerToggle"}
#     _accounts_button = {"by": By.NAME, "value": "Accounts"}
#     _customers_button = {"by": By.NAME, "value": "Customers"}
#
#     # def ___init___(self, driver):
#     #     self.driver = driver
#
#     def with_(self):
#         assert self._find(self._customers_page)
#         self._click(self._submit_button)
#
#     def customers_page_link_present(self):
#         return self._get_title(self._success_message, config.login_success_timeout)
#     #
#     # def failure_message_present(self):
#     #     return self._is_displayed(self._failure_message, 1)
#
#     # def test_invalid_credentials(self, login):
#     #     login.with_("tomsmith", "bad password")
#     #     assert login.failure_message_present()