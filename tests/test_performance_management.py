import time

import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from pages.dashboard import DashboardPage
from pages.login_page import LoginPage
from pages.performance_page import PerformancePage


scenarios("../features/performance_management.feature")


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def performance_page(page):
    return PerformancePage(page)

@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)


@given("user is logged in as admin")
def user_logged_in_as_admin(login_page):
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    usr_name = "Admin"
    usr_pass = "admin123"
    login_page.navigate(url)
    login_page.login(usr_name, usr_pass)


@given("user navigates to Performance module")
def navigate_to_performance_module(dashboard_page, performance_page):
    dashboard_page.verify_dashboard_loaded()
    dashboard_page.navigate_to_module("Performance")
    performance_page.verify_performance_page_loaded()



@when('user clicks on Manage Reviews')
def click_manage_reviews(performance_page):
    performance_page.click_manage_reviews()


@when('user clicks on Add button')
def click_add_button(performance_page):
    performance_page.click_add_button()


@when(parsers.parse('user selects employee "{employee_name}"'))
def select_employee(performance_page, employee_name):
    performance_page.select_employee(employee_name)



@when(parsers.parse('user selects review period "{review_period}"'))
def select_review_period(performance_page, review_period):
    performance_page.select_review_period(review_period)


@when(parsers.parse('user selects supervisor "{supervisor_name}"'))
def select_supervisor(performance_page, supervisor_name):
    """Select supervisor from dropdown"""
    performance_page.select_supervisor(supervisor_name)


@when(parsers.parse('user selects due date "{due_date}"'))
def select_due_date(performance_page, due_date):
    """Select due date"""
    performance_page.select_due_date(due_date)


@when(parsers.parse('user clicks on save button'))
def click_save_button(performance_page):
    """Click save button"""
    performance_page.click_save_button()

@then("performance review should be created successfully")
def verify_review_created(performance_page):
    performance_page.verify_success_message()


# @then("review should appear in reviews list")
# def verify_review_in_list(performance_page):
#     """Verify review appears in the list"""
#     performance_page.verify_review_exists_in_list()
#
#
# @then(parsers.parse('review status should be "{status}"'))
# def verify_review_status(performance_page, status):
#     """Verify review status"""
#     performance_page.verify_review_status(status)


