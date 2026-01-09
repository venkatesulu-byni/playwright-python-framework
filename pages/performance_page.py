import time
from time import sleep

from pages.base_page import BasePage
from playwright.sync_api import Page, expect

from utils.utils import quarter_to_dates


class PerformancePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Locators
        self.performance_header = page.get_by_role("heading", name="Performance")
        self.manage_reviews_nav = page.locator(".oxd-topbar-body-nav-tab-item").filter(has_text="Manage Reviews")
        self.manage_reviews_tab = page.get_by_role("menuitem", name="Manage Reviews")
        self.add_button = page.get_by_role("button", name="Add")
        self.employee_name_label = page.get_by_text("Employee Name")
        self.employee_dropdown = page.get_by_placeholder("Type for hints...").nth(0)
        self.review_period_start_dropdown = page.get_by_placeholder("yyyy-dd-mm").nth(0)
        self.review_period_end_dropdown = page.get_by_placeholder("yyyy-dd-mm").nth(1)
        self.supervisor_dropdown = page.get_by_placeholder("Type for hints...").nth(1)
        self.due_date_input = page.get_by_placeholder("yyyy-dd-mm").nth(2)
        self.save_button = page.get_by_role("button", name="Save")
        self.dynamic_drop_down = page.get_by_role("option")

        self.success_message = page.locator(".oxd-toast-content--success")
        self.reviews_list = "//table[@id='reviewsList'] | //div[contains(@class, 'reviews-list')]"
        self.configure_menu = "//a[text()='Configure']"
        self.kpis_menu = "//a[text()='KPIs']"
        self.kpi_title_input = "//input[@id='kpiTitle' or @name='title']"
        self.job_title_dropdown = "//select[@id='jobTitle']"



    def click_manage_reviews(self):
        self.manage_reviews_nav.click()
        self.manage_reviews_tab.click()

    def click_add_button(self):
        self.add_button.click()
        expect(self.employee_name_label).to_be_visible()


    def select_employee(self, employee_name):
        self.employee_dropdown.type(employee_name)
        time.sleep(2)
        print(self.dynamic_drop_down.inner_html())
        self.dynamic_drop_down.locator("//span").nth(0).click()
        # print(self.dynamic_drop_down.inner_html())


    def select_review_period(self, review_period):
        start, end = quarter_to_dates(review_period)
        self.review_period_start_dropdown.fill(start)
        self.review_period_end_dropdown.fill(end)

    def select_supervisor(self, supervisor_name: str):
        self.supervisor_dropdown.fill(supervisor_name)
        time.sleep(2)
        self.dynamic_drop_down.locator("//span").nth(0).click()

    def select_due_date(self, due_date):
        self.due_date_input.fill(due_date)

    def click_save_button(self):
        self.save_button.click()


    def verify_performance_page_loaded(self):
        expect(self.performance_header).to_be_visible()


    def verify_success_message(self):
        expect(self.success_message).to_contain_text("Successfully Updated")

    def verify_review_exists_in_list(self):
        """Verify review appears in the list"""
        self.wait_for_element(self.reviews_list)
        expect(self.page.locator(self.reviews_list)).to_be_visible()

    def verify_review_status(self, expected_status: str):
        """Verify review status"""
        status_locator = f"//td[contains(text(), '{expected_status}')] | //span[contains(text(), '{expected_status}')]"
        self.wait_for_element(status_locator)
        actual_status = self.get_text(status_locator)
        assert expected_status in actual_status, \
            f"Expected status '{expected_status}' but got '{actual_status}'"

    def navigate_to_configure(self):
        """Navigate to Configure section"""
        self.click(self.configure_menu)
        self.wait_for_page_load()

    def click_kpis(self):
        """Click on KPIs menu"""
        self.click(self.kpis_menu)
        self.wait_for_page_load()

    def enter_kpi_title(self, kpi_title: str):
        """Enter KPI title"""
        self.fill(self.kpi_title_input, kpi_title)

    def select_job_title(self, job_title: str):
        """Select job title"""
        self.select_dropdown_option(self.job_title_dropdown, job_title)

    def verify_kpi_success_message(self):
        """Verify KPI success message"""
        self.verify_success_message()

    def verify_kpi_in_list(self):
        """Verify KPI appears in the list"""
        kpi_list = "//table[@id='kpiList'] | //div[contains(@class, 'kpi-list')]"
        self.wait_for_element(kpi_list)
        expect(self.page.locator(kpi_list)).to_be_visible()