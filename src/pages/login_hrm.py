from src.pages.dashboard import DashboardPage


class LoginPage:
    def __init__(self, page):
        self.page = page

        self.username = page.locator('//input[@name="username"]')
        self.password = page.locator('//input[@name="password"]')
        self.forgot_pass = page.get_by_text("Forgot your password?")
        self.login_btn = page.get_by_role("button", name="Login")


    def navigate(self, url):
        self.page.goto(url)

    def login(self, usr_name, usr_pass):
        self.username.fill(usr_name)
        self.password.fill(usr_pass)
        self.login_btn.click()
        dashboard = DashboardPage(self.page)
        return dashboard

    def forgot_password(self):
        self.forgot_pass.click()