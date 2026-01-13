import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser to run tests on"
    )

    parser.addoption(
        "--headless",
        action="store",
        default="true",
        choices=["true", "false"],
        help="Run browser in headless mode (true/false)"
    )



@pytest.fixture(scope="session")
def browser(playwright, request):
    browser_name = request.config.getoption("--browser_name")
    headless_option = request.config.getoption("--headless").lower() == "true"

    if browser_name == "firefox":
        browser = playwright.firefox.launch(headless=headless_option)
    else:
        browser = playwright.chromium.launch(headless=headless_option)

    yield browser
    browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page