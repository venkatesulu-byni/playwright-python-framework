import time
from idlelib.search import SearchDialog
from re import search

from mako.testing.assertions import expect_raises_message_with_proper_context
from playwright.sync_api import expect

from pages.base_page import BasePage


class PIMPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.pim_header = page.get_by_role("heading", name="PIM")
        self.add_employee_tab = page.get_by_role("link", name="Add Employee")
        self.employee_name_label = page.get_by_text("Employee Full Name")
        self.first_name_input = page.get_by_role("textbox", name="First Name")
        self.middle_name_input = page.get_by_role("textbox", name="Middle Name")
        self.last_name_input = page.get_by_role("textbox", name="Last Name")
        self.employee_id_input = page.locator("//input").nth(5)
        self.save_button = page.get_by_role("button", name="Save")
        self.success_message = page.locator(".oxd-toast-content--success")
        self.delete_button = page.get_by_role("button", name="Delete Selected")
        self.confirm_delete_button = page.get_by_role("button", name="Yes, Delete")
        self.emp_header = page.locator(".oxd-text.oxd-text--h6.--strong")
        self.dynamic_drop_down = page.get_by_role("option")

        # Search page
        self.emp_name_search_box = page.get_by_role("textbox").nth(1)
        self.emp_id_search_box = page.get_by_role("textbox").nth(2)
        self.search_method = ''
        self.search_button = page.get_by_role("button", name="Search")

    def click_add_employee(self):
        self.add_employee_tab.click()
        expect(self.employee_name_label).to_be_visible()

    def fill_employee_details(self, first_name: str, middle_name: str,
                              last_name: str, employee_id: str):
        self.first_name_input.fill(first_name)
        if middle_name:
            self.middle_name_input.fill(middle_name)
        self.last_name_input.fill(last_name)
        self.employee_id_input.clear()
        self.employee_id_input.fill(employee_id)

    def save_employee(self):
        self.save_button.click()

    def search_employee(self, search_value: str):
        if self.search_method == "Employee Name":
            self.emp_name_search_box.fill(search_value)
            time.sleep(2)
            self.dynamic_drop_down.locator("//span").nth(0).click()

        elif self.search_method == "Employee Id":
            self.emp_id_search_box.fill(search_value)

    def search_employee_name(self, employee_name):
        self.search_method = 'Employee Name'
        self.search_employee(employee_name)
        self.click_search()
        self.verify_emp_details(employee_name)

    def get_employee_record(self, employee_name):
        self.search_employee_name(employee_name)
        return self.page.locator(".oxd-table-card").first

    def verify_emp_details(self, employee):
        record = self.page.locator(".oxd-table-card").first
        expect(record).to_contain_text(employee)

    def select_employee_checkbox(self, employee):
        record = self.get_employee_record(employee)
        record.locator('label').click()

    def click_delete(self):
        self.delete_button.click()

    def click_search(self):
        self.search_button.click()

    def confirm_deletion(self):
        self.confirm_delete_button.click()
        self.page.wait_for_load_state("networkidle")


    def verify_pim_module_loaded(self):
        expect(self.pim_header).to_be_visible()
