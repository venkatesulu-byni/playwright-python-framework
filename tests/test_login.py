import re

from playwright.sync_api import expect
from pytest_bdd import scenarios
from pytest_bdd import given, when, then, parsers

from pages.dashboard import DashboardPage
from pages.forgot_password import ForgotPasswordPage
from pages.login_page import LoginPage

scenarios("../features/login.feature")

def normalize_empty(value):
    return "" if value.strip().upper() == "EMPTY" else value

@given(parsers.parse('user navigates to OrangeHRM login page "{url}"'))
def open_login_page(page, url):
    page.goto(url)

@when(parsers.parse('user enters username "{username}"'))
def enter_username(page, username):
    LoginPage(page).enter_username(normalize_empty(username))

@when(parsers.parse('user enters password "{password}"'))
def enter_password(page, password):
    LoginPage(page).enter_password(normalize_empty(password))

@when("user clicks on login button")
def click_login(page):
    LoginPage(page).click_login()


@then("user should be redirected to dashboard page")
def verify_dashboard_url(page):
    expect(page).to_have_url(re.compile(r".*/dashboard/index$"), timeout=30000)


@then("user should see Dashboard")
def verify_dashboard_visible(page):
    DashboardPage(page).verify_dashboard_loaded()


@then(parsers.parse('user should see error message "{error_message}"'))
def verify_error_message(page, error_message):
    LoginPage(page).verify_error_message_displayed(error_message)


@then("user should remain on login page")
def verify_login_page(page):
    LoginPage(page).verify_login_page_loaded()


@then(parsers.parse('user should see validation message "{username_error}" for username field'))
def verify_username_validation(page, username_error):
    username_error = username_error.strip() if username_error else ""
    if username_error and username_error.upper() != "NA":
        LoginPage(page).verify_username_required()


@then(parsers.parse('user should see validation message "{password_error}" for password field'))
def verify_password_validation(page, password_error):
    password_error = password_error.strip() if password_error else ""
    if password_error and password_error.upper() != "NA":
        LoginPage(page).verify_password_required()

@when('user clicks on "Forgot your password?" link')
def click_forgot_password(page):
    LoginPage(page).forgot_password()


@then('user should be redirected to reset password page')
def verify_forgot_pass_page(page):
    ForgotPasswordPage(page).verify_forgot_password_page_loaded()


@then('user should see username field for password reset')
def verify_username_field(page):
    ForgotPasswordPage(page).verify_username_field_present()