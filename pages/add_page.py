from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from pages.base_page import BasePage
from tests import config

import sys
sys.path.append(sys.path[0] + "../../../")


class AddPage(BasePage):
    _username_input = {"by": By.NAME, "value": "email"}
    _password_input = {"by": By.NAME, "value": "password"}
    _submit_button = {"by": By.CSS_SELECTOR, "value": "button"}
    _success_message = {"value": "Dashboard"}
    _login_page_title = {"value": "Login"}
    _accounts_button = {"by": By.CSS_SELECTOR, "value": '#drawerAccordion > div > div > a:nth-child(10)'}
    _customers_button = {"by": By.LINK_TEXT, "value": "Customers"}
    _customers_page_title = {"value": "Customers"}
    _add_button = {"by": By.CSS_SELECTOR, "value": '#layoutDrawer_content > main > div > header > div > div > div.col-12.col-md-auto.flex-shrink-0 > form > button'}
    _add_customer_page_title = {"value": "Add Customer"}
    _firstname_input = {"by": By.NAME, "value": "fname"}
    _lastname_input = {"by": By.NAME, "value": "lname"}
    _email_input = {"by": By.NAME, "value": "email"}
    _new_password_input = {"by": By.NAME, "value": "password"}
    _mobile_number_input = {"by": By.NAME, "value": "mobile"}
    _address1_input = {"by": By.NAME, "value": "address1"}
    _address2_input = {"by": By.NAME, "value": "address2"}
    _setting_balance = {"by": By.NAME, "value": "balance"}
    _country_button = {"by": By.XPATH, "value": '//span[text()="Please Select"]'}
    _country_input = {"by": By.XPATH, "value": "//div[contains( text(),'Algeria')]"}
    _sub_checkbox = {"by": By.NAME, "value": "newssub"}
    _status_select = {"by": By.NAME, "value": "status"}
    _currency_select = {"by": By.NAME, "value": "currency"}
    _update_button = {"by": By.CSS_SELECTOR, "value": '#layoutDrawer_content > main > div > form > div > div.col-lg-8 > div > div > div.text-end > button'}
    _table_tag = {"by": By.CSS_SELECTOR,
                  "value": '#layoutDrawer_content > main > div > div.xcrud > div > div.xcrud-ajax > div.xcrud-list-container > table'}
    _alert_danger_messsage = {"by": By.CSS_SELECTOR, "value": ".alert.alert-danger"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("/api/admin/accounts/customers/")
        assert self._get_title(self._login_page_title)

    def with_(self, username, password):
        self._type(self._username_input, username)
        self._type(self._password_input, password)
        self._click(self._submit_button)


    def login_success_check(self):
        return self._get_title(self._success_message, config.login_success_timeout)

    def goto_customers_page(self):
        self._click(self._accounts_button)
        self._click_inarow(self._customers_button, config.login_success_timeout)
        return self._get_title(self._customers_page_title, config.login_success_timeout)

    def goto_add_page(self):
        self._click(self._add_button)
        return self._get_title(self._add_customer_page_title, config.add_customer_page_timeout)

    def is_customers_page(self):
        return self._get_title(self._customers_page_title, config.login_success_timeout)

    def is_not_customers_page(self):
        return self._cannot_get_title(self._customers_page_title, 1)

    def insert_data(self, firstname, lastname, email, password, mobile,
                          country, address1, address2, status, currency, balance):
        self._type(self._firstname_input, firstname)
        self._type(self._lastname_input, lastname)
        self._type(self._email_input, email)
        self._type(self._new_password_input, password)
        self._type(self._mobile_number_input, mobile)
        self._click(self._country_button)
        self._click_inarow2(self._country_input, config.login_success_timeout)
        self._type(self._address1_input, address1)
        self._type(self._address2_input, address2)
        self._click(self._sub_checkbox)
        self._select(self._status_select, status)
        self._select(self._currency_select, currency)
        self._type(self._setting_balance, balance)
        self._click(self._update_button)

        return True

    def is_firstname_inserted(self, firstname):
        _table = self._find(self._table_tag)
        _tbody = _table.find_element(By.TAG_NAME, "tbody")
        for tr in _tbody.find_elements(By.TAG_NAME, "tr"):
            td = tr.find_elements(By.TAG_NAME, "td")
            if td[2].text == firstname:
                return True
        return False

    def is_lastname_inserted(self, lastname):
        _table = self._find(self._table_tag)
        _tbody = _table.find_element(By.TAG_NAME, "tbody")
        for tr in _tbody.find_elements(By.TAG_NAME, "tr"):
            td = tr.find_elements(By.TAG_NAME, "td")
            if td[3].text == lastname:
                return True
        return False

    def is_email_inserted(self, email):
        _table = self._find(self._table_tag)
        _tbody = _table.find_element(By.TAG_NAME, "tbody")
        for tr in _tbody.find_elements(By.TAG_NAME, "tr"):
            td = tr.find_elements(By.TAG_NAME, "td")
            if td[4].text == email:
                return True
        return False

    def is_balance_inserted(self, balance):
        _table = self._find(self._table_tag)
        _tbody = _table.find_element(By.TAG_NAME, "tbody")
        for tr in _tbody.find_elements(By.TAG_NAME, "tr"):
            td = tr.find_elements(By.TAG_NAME, "td")
            if td[5].text == balance:
                return True
        return False

    def is_currency_inserted(self, currency):
        _table = self._find(self._table_tag)
        _tbody = _table.find_element(By.TAG_NAME, "tbody")
        for tr in _tbody.find_elements(By.TAG_NAME, "tr"):
            td = tr.find_elements(By.TAG_NAME, "td")
            if td[6].text == currency:
                return True
        return False

    def is_status_inserted(self, email, status):
        _table = self._find(self._table_tag)
        _tbody = _table.find_element(By.TAG_NAME, "tbody")
        for tr in _tbody.find_elements(By.TAG_NAME, "tr"):
            td = tr.find_elements(By.TAG_NAME, "td")
            if td[4].text == email:
                if status == 'Enabled':
                    try:
                        status = td[7].find_element(By.CSS_SELECTOR, ".fa.fa-times.text-success")

                    except NoSuchElementException:
                        return False

                    return True
                else:
                    try:
                        status = td[7].find_element(By.CSS_SELECTOR, ".fa.fa-times.text-success")

                    except NoSuchElementException:
                        return True

                    return False

    def delete_input_data(self, email):
        _table = self._find(self._table_tag)
        _tbody = _table.find_element(By.TAG_NAME, "tbody")
        for tr in _tbody.find_elements(By.TAG_NAME, "tr"):
            td = tr.find_elements(By.TAG_NAME, "td")
            if td[4].text == email:
                td[9].find_elements(by=By.TAG_NAME, value="a")[1].click()

                Alert(self.driver).accept()
                self.is_customers_page()
                return True




    def fetch_edit_button(self, email):
        _table = self._find(self._table_tag)
        _tbody = _table.find_element(By.TAG_NAME, "tbody")
        for tr in _tbody.find_elements(By.TAG_NAME, "tr"):
            td = tr.find_elements(By.TAG_NAME, "td")
            if td[4].text == email:
                _edit_button = td[9].find_elements(by=By.TAG_NAME, value="a")[0]

        # self._click(self._edit_button)
        # self._find(self._firstname_input)
        return 1

    def alert_danger_message_present(self):
         return self._is_displayed(self._alert_danger_messsage, 1)

    def alert_danger_message_not_present(self):
         return self._is_not_displayed(self._alert_danger_messsage, 1)















