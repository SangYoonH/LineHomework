import pytest
from pages import edit_page
from . import config


@pytest.fixture
def edit(driver):

    edit_object = edit_page.EditPage(driver)
    yield edit_object
    edit_object._visit("https://phptravels.net/api/admin/accounts/customers/")
    edit_object.delete_input_data(config.valid_email_address)

@pytest.mark.order(8)
def test_duplicated_email_edit_customer(edit):
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
    assert edit.edit_email_data(config.edit_valid_email_address)
    assert edit.alert_danger_message_present()
    assert edit.is_not_customers_page()













