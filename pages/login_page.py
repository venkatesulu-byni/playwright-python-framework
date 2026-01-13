from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.login_banner = page.get_by_role("heading", name="Login")
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.get_by_role("alert")
        self.forgot_password_link = page.get_by_role("link", name="Forgot your password?")
        self.required_errors = page.get_by_text("Required")
        self.forgot_pass = page.get_by_text("Forgot your password?")
        self.username_error = ''

    def enter_username(self, username: str):
        self.username_input.fill(username)

    def enter_password(self, password: str):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


    def forgot_password(self):
        self.forgot_pass.click()

    def verify_error_message_displayed(self, error_msg):
        self.expect_visible(self.error_message)
        assert self.error_message.text_content() == error_msg

    def verify_username_required(self):
        self.username_error = True
        self.expect_visible(self.required_errors.nth(0))

    def verify_password_required(self):
        if self.username_error:
            self.expect_visible(self.required_errors.nth(1))
        else:
            self.expect_visible(self.required_errors.nth(0))

    def verify_login_page_loaded(self):
        expect(self.login_banner).to_be_visible()