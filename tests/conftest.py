import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action='store', default='chrome', help="List of available browsers are chrome & firefox"
    )
    pass


@pytest.fixture(scope='session')
def browser_instance(playwright, request):
    browser_name = request.config.getoption('browser_name')
    print("Browser selected:", browser_name)
    if browser_name == 'firefox':
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == 'chrome':
        browser = playwright.chromium.launch(headless=False)
    else:
        browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()