import pytest
from pages import edit_page
from . import config


@pytest.fixture
def edit(driver):
    edit_object = edit_page.EditPage(driver)
    yield edit_object
    edit_object.goto_customers_page()
    edit_object.delete_input_data(config.valid_email_address)
    edit_object.delete_input_data(config.edit_valid_email_address)


@pytest.mark.order(7)
def test_valid_edit_customer(edit):
    edit.with_(config.valid_username, config.valid_password)
    assert edit.login_success_check()
    assert edit.goto_customers_page()
    assert edit.goto_add_page()
    edit.insert_data(config.first_name, config.last_name, config.valid_email_address,
                     config.valid_new_password, config.mobile_number, config.country, config.address_1,
                     config.address_2, config.setting_status,
                     config.setting_currency, config.setting_balance)
    assert edit.alert_danger_message_not_present()
    assert edit.is_customers_page()
    assert edit.fetch_edit_button_and_click(config.valid_email_address)
    assert edit.is_update_page()
    edit.edit_data(config.edit_first_name, config.edit_last_name, config.edit_valid_email_address,
                   config.edit_valid_new_password, config.edit_mobile_number, config.edit_country,
                   config.edit_address_1,
                   config.edit_address_2, config.edit_setting_status, config.edit_setting_currency,
                   config.edit_setting_balance)
    assert edit.alert_danger_message_not_present()
    assert edit.is_customers_page()
    assert edit.is_firstname_inserted(config.edit_first_name)
    assert edit.is_lastname_inserted(config.edit_last_name)
    assert edit.is_email_inserted(config.edit_valid_email_address)
    assert edit.is_balance_inserted(config.edit_setting_balance)
    assert edit.is_currency_inserted(config.edit_setting_currency)
    assert edit.is_status_inserted(config.edit_valid_email_address, config.edit_setting_status)
