Feature: Employee Management (PIM)

  Background:
    Given user is logged in as admin
    And user navigates to PIM module

  Scenario Outline: Add new employee with different data
    When user clicks on Add Employee tab
    And user enters first name "<first_name>"
    And user enters middle name "<middle_name>"
    And user enters last name "<last_name>"
    And user enters employee id "<employee_id>"
    And user clicks on save button
    Then employee should be added successfully
    And user should see success message "Successfully Saved"
    And employee "<first_name> <last_name>" should be displayed

    Examples:
      | first_name | middle_name | last_name | employee_id |
      | John       | Michael     | Doe       | EMP001      |
      | Jane       | Marie       | Smith     | EMP002      |
      | Robert     | James       | Wilson    | EMP003      |
      | Sarah      | Ann         | Johnson   | EMP004      |

  Scenario Outline: Search employee by different criteria
    When user selects search criteria "<search_by>"
    And user enters search value "<search_value>"
    And user clicks on search button
    Then search results should display matching employees
    And results should contain "<expected_result>"

    Examples:
      | search_by      | search_value     | expected_result  |
      | Employee Name  | John Michael Doe | John Michael |
      | Employee Id    | EMP001           | EMP001           |


  Scenario Outline: Delete employee record
    Given employee "<employee_Name>" exists in system
    When user selects employee "<employee_Name>" checkbox
    And user clicks on delete button
    And user confirms deletion
    Then employee should be deleted successfully
    And user should see success message "Successfully Deleted"
    And employee "<employee_Name>" should not appear in employee list

    Examples:
      | employee_Name |
      | John Michael  |
      | Jane Marie    |
      | Robert James  |
      | Sarah Ann     |