import pytest
from pages import add_page
from . import config


@pytest.fixture
def add(driver):

    add_object = add_page.AddPage(driver)
    yield add_object
    add_object._visit("https://phptravels.net/api/admin/accounts/customers/")
    add_object.delete_input_data(config.valid_email_address)


def test_invalid_email_add_customer(add):
    add.with_(config.valid_username, config.valid_password)
    assert add.login_success_check()
    assert add.goto_customers_page()
    assert add.goto_add_page()
    assert add.insert_data(config.first_name, config.last_name, config.invalid_email_address,
                          config.valid_new_password, config.mobile_number, config.country, config.address_1,
                          config.address_2, config.setting_status,
                          config.setting_currency, config.setting_balance)
    assert add.is_not_customers_page()











