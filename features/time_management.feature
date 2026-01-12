Feature: Time Management

  Background:
    Given user is logged in as employee
    And user navigates to Time module

  Scenario Outline: Record time for different projects
    When user clicks on My Timesheets
    And user selects date "<date>"
    And user selects project "<project_name>"
    And user selects activity "<activity>"
    And user enters hours "<hours>" for "<day>"
    And user clicks on save button
    Then timesheet should be saved successfully
    And total hours for the day should display as "<hours>"

    Examples:
      | date       | project_name      | activity    | hours | day       |
      | 2026-02-03 | Internal Projects | Development | 8     | Monday    |
      | 2026-02-04 | Client Project A  | Testing     | 6     | Tuesday   |
      | 2026-02-05 | Internal Projects | Code Review | 4     | Wednesday |
      | 2026-02-06 | Client Project B  | Deployment  | 8     | Thursday  |

  Scenario: Submit timesheet for approval
    Given user has recorded time for current week
    When user reviews timesheet entries
    And user clicks on submit button
    Then timesheet should be submitted for approval
    And timesheet status should change to "Submitted"
    And user should see success message

  Scenario Outline: Approve or reject timesheet as supervisor
    Given user is logged in as supervisor
    And there are submitted timesheets from "<employee_name>"
    When user navigates to timesheets to approve
    And user selects timesheet from "<employee_name>"
    And user clicks on "<action>" button
    Then timesheet status should change to "<final_status>"
    And employee should receive notification

    Examples:
      | employee_name | action  | final_status |
      | John Doe      | Approve | Approved     |
      | Jane Smith    | Reject  | Rejected     |