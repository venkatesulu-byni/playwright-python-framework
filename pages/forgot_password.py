from playwright.sync_api import expect

from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.page = page
        self.reset_label = page.get_by_role("heading", name="Reset Password")
        self.cancel_btn = page.locator('//button[normalize-space()="Cancel"]')
        self.reset_btn = page.get_by_role("button", name="Reset Password")
        self.user_name = page.get_by_placeholder("Username")


    def cancel(self):
        self.cancel_btn.click()


    def rest_password(self, usr_name):
        self.user_name.fill(usr_name)
        self.reset_btn.click()

    def verify_forgot_password_page_loaded(self):
        expect(self.reset_label).to_be_visible()

    def verify_username_field_present(self):
        expect(self.user_name).to_be_visible()
