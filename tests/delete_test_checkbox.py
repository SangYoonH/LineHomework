import sys
sys.path.append(sys.path[0] + "../../../")

import pytest
from pages import customer_page
from . import config


@pytest.fixture
def delete(driver):

    delete_object = customer_page.CustomerPage(driver)
    yield delete_object
    # delete_object._visit("https://phptravels.net/api/admin/accounts/customers/")
    # delete_object.delete_input_data(config.valid_email_address)


def test_delete_checkbox_customer(delete):
    delete.with_(config.valid_username, config.valid_password)
    assert delete.login_success_check()
    assert delete.goto_customers_page()
    assert delete.goto_add_page()
    delete.insert_data(config.first_name, config.last_name, config.valid_email_address,
                    config.valid_new_password, config.mobile_number, config.country, config.address_1,
                    config.address_2, config.setting_status,
                    config.setting_currency, config.setting_balance)
    assert delete.alert_danger_message_not_present()
    assert delete.is_customers_page()
    assert delete.get_checkbox_and_click(config.valid_email_address)
    assert delete.delete_checked_data()
    assert delete.is_email_deleted(config.valid_email_address)












