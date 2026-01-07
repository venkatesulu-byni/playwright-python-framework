from playwright.sync_api import expect

from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

        self.usr_profile_dropdown = page.locator(".oxd-userdropdown-name")
        self.logout_menu = page.get_by_role("menuitem", name="Logout")


    def click_on_profile_drop_down(self):
        self.usr_profile_dropdown.click()

    def click_on_logout(self):
        self.logout_menu.click()

    def assert_dashboard_loaded(self):
        expect(self.page.get_by_role("heading", name="Dashboard")).to_be_visible()

