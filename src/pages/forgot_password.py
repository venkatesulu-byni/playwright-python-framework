from src.pages.login_hrm import LoginPage


class ForgotPasswordPage:
    def __init__(self, page):
        self.page = page
        self.reset_label = page.get_by_role("heading", name="Reset Password")
        self.cancel_btn = page.locator('//button[normalize-space()="Cancel"]')
        self.reset_btn = page.get_by_role("button", name="Reset Password")
        self.user_name = page.get_by_placeholder("Username")


    def cancel(self):
        self.cancel_btn.click()
        login_page = LoginPage(self.page)
        return login_page

    def rest_password(self, usr_name):
        self.user_name.fill(usr_name)
        self.reset_btn.click()
