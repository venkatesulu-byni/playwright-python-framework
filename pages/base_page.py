from playwright.sync_api import Page, expect
import logging

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(self.__class__.__name__)

    def navigate(self, url: str):
        self.page.goto(url)
        self.logger.info(f"Navigated to: {url}")

    def current_url(self) -> str:
        return self.page.url

    def expect_visible(self, locator):
        expect(locator).to_be_visible()

    def expect_text(self, locator, text: str):
        expect(locator).to_contain_text(text)
