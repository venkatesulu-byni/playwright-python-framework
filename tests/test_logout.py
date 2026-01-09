import re

from playwright.sync_api import expect
from pytest_bdd import scenarios, given, when, then

from pages.dashboard import DashboardPage
from pages.login_page import LoginPage

scenarios("../features/logout.feature")

@given("user is logged in to OrangeHRM application")
def login_to_hrm(page):
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    usr_name = "Admin"
    usr_pass = "admin123"
    login_page = LoginPage(page)
    login_page.navigate(url)
    login_page.login(usr_name, usr_pass)
    DashboardPage(page).verify_dashboard_loaded()

@when("user clicks on user profile dropdown")
def click_on_usr_profile(page):
    DashboardPage(page).click_on_profile_drop_down()

@when("user clicks on logout option")
def click_on_logout(page):
    DashboardPage(page).click_on_logout()

@then("user should be logged out successfully")
def  user_logout(page):
    expect(page).to_have_url(re.compile(r".*/auth/login$"), timeout=30000)

@then("user should be redirected to login page")
def redirect_to_login_page(page):
    LoginPage(page).verify_login_page_loaded()


