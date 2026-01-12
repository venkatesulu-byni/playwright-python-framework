import time

import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page, expect

from pages.dashboard import DashboardPage
from pages.login_page import LoginPage
from pages.pim_page import PIMPage

# Load scenarios from feature file
scenarios('../features/employee_management.feature')


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)


@pytest.fixture
def pim_page(page):
    return PIMPage(page)


@given("user is logged in as admin")
def user_logged_in(login_page):
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    usr_name = "Admin"
    usr_pass = "admin123"
    login_page.navigate(url)
    login_page.login(usr_name, usr_pass)


@given("user navigates to PIM module")
def navigate_to_pim(dashboard_page, pim_page):
    dashboard_page.verify_dashboard_loaded()
    dashboard_page.navigate_to_module("PIM")
    pim_page.verify_pim_module_loaded()


@when("user clicks on Add Employee tab")
def click_add_employee(pim_page):
    pim_page.click_add_employee()


@when(parsers.parse('user enters first name "{first_name}"'))
def enter_first_name(pim_page, first_name):
    pim_page.first_name_input.fill(first_name)


@when(parsers.parse('user enters middle name "{middle_name}"'))
def enter_middle_name(pim_page, middle_name):
    if middle_name:
        pim_page.middle_name_input.fill(middle_name)


@when(parsers.parse('user enters last name "{last_name}"'))
def enter_last_name(pim_page, last_name):
    pim_page.last_name_input.fill(last_name)


@when(parsers.parse('user enters employee id "{employee_id}"'))
def enter_employee_id(pim_page, employee_id):
    pim_page.employee_id_input.clear()
    pim_page.employee_id_input.fill(employee_id)


@when("user clicks on save button")
def click_save(pim_page):
    pim_page.save_employee()


@then("employee should be added successfully")
def verify_employee_added(pim_page):
    expect(pim_page.success_message).to_be_visible(timeout=10000)


@then(parsers.parse('user should see success message "{message}"'))
def verify_success_message(pim_page, message):
    expect(pim_page.success_message).to_contain_text(message)


@then(parsers.parse('employee "{employee_name}" should be displayed'))
def verify_employee_displayed(pim_page, employee_name):
    expect(pim_page.emp_header).to_contain_text(employee_name)


@when(parsers.parse('user selects search criteria "{search_by}"'))
def select_search_criteria(pim_page, search_by):
    pim_page.search_method = search_by


@when(parsers.parse('user enters search value "{search_value}"'))
def enter_search_value(pim_page, search_value):
    pim_page.search_employee(search_value)


@when("user clicks on search button")
def click_search(pim_page):
    pim_page.click_search()


@then("search results should display matching employees")
def verify_search_results(page):
    results = page.locator(".oxd-table-card")
    expect(results.first).to_be_visible(timeout=10000)


@then(parsers.parse('results should contain "{expected_result}"'))
def verify_search_contains(pim_page, expected_result):
    pim_page.verify_emp_details(expected_result)


@given(parsers.parse('employee "{employee_name}" exists in system'))
def employee_exists(pim_page, employee_name):
    pim_page.search_employee_name(employee_name)


@when(parsers.parse('user selects employee "{employee_name}" checkbox'))
def select_employee(pim_page, employee_name):
    pim_page.select_employee_checkbox(employee_name)


@when("user clicks on delete button")
def click_delete_button(pim_page):
    pim_page.click_delete()


@when("user confirms deletion")
def confirm_deletion(pim_page):
    pim_page.confirm_deletion()


@then("employee should be deleted successfully")
def verify_employee_deleted(pim_page):
    expect(pim_page.success_message).to_be_visible(timeout=10000)


@then(parsers.parse('employee "{employee_name}" should not appear in employee list'))
def verify_employee_not_in_list(pim_page, employee_name):
    pim_page.emp_name_search_box.fill(employee_name)
    time.sleep(2)
    expect(pim_page.dynamic_drop_down).to_contain_text("No Records Found")
