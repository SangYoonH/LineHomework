import pytest
from pages import add_page
from . import config


@pytest.fixture
def add(driver):
    add_object = add_page.AddPage(driver)
    yield add_object
    add_object.delete_input_data(config.valid_email_address)


@pytest.mark.order(2)
def test_valid_add_customer(add):
    add.with_(config.valid_username, config.valid_password)
    assert add.login_success_check()
    assert add.goto_customers_page()
    assert add.is_customers_page()
    assert add.goto_add_page()
    add.insert_data(config.first_name, config.last_name, config.valid_email_address,
                           config.valid_new_password, config.mobile_number, config.country, config.address_1,
                           config.address_2, config.setting_status,
                           config.setting_currency, config.setting_balance)
    assert add.alert_danger_message_not_present()
    assert add.is_customers_page()
    assert add.is_firstname_inserted(config.first_name)
    assert add.is_lastname_inserted(config.last_name)
    assert add.is_email_inserted(config.valid_email_address)
    assert add.is_balance_inserted(config.setting_balance)
    assert add.is_currency_inserted(config.setting_currency)
    assert add.is_status_inserted(config.valid_email_address, config.setting_status)
