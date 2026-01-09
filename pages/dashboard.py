from playwright.sync_api import expect

from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

        self.usr_profile_dropdown = page.locator(".oxd-userdropdown-name")
        self.logout_menu = page.get_by_role("menuitem", name="Logout")
        self.module_pim = page.get_by_role("link", name="PIM")
        self.module_performance = page.get_by_role("link", name="Performance")


    def navigate_to_module(self, module_name):
        if module_name == "PIM":
            self.module_pim.click()
        elif module_name == "Performance":
            self.module_performance.click()


    def click_on_profile_drop_down(self):
        self.usr_profile_dropdown.click()

    def click_on_logout(self):
        self.logout_menu.click()

    def verify_dashboard_loaded(self):
        expect(self.page.get_by_role("heading", name="Dashboard")).to_be_visible()

