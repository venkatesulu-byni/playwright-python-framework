Feature: Leave Management

  Background:
    Given user is logged in as employee
    And user navigates to Leave module

  Scenario Outline: Apply for different types of leave
    When user clicks on Apply Leave button
    And user selects leave type "<leave_type>"
    And user selects from date as "<from_date>"
    And user selects to date as "<to_date>"
    And user enters comments "<comments>"
    And user clicks on apply button
    Then leave request should be submitted successfully
    And user should see success message "Successfully Saved"
    And leave status should show as "Pending Approval"
    And leave duration should be "<duration>" days

    Examples:
      | leave_type        | from_date  | to_date    | comments              | duration |
      | Sick Leave        | 2026-02-01 | 2026-02-03 | Medical appointment   | 3        |
      | Casual Leave      | 2026-03-10 | 2026-03-10 | Personal work         | 1        |
      | Annual Leave      | 2026-04-15 | 2026-04-20 | Vacation              | 6        |
      | Maternity Leave   | 2026-05-01 | 2026-07-31 | Maternity             | 92       |

  Scenario: View leave balance
    When user clicks on Leave List
    And user views leave balance section
    Then user should see available leave balance for each leave type
    And leave balance should display correct numbers

  Scenario Outline: Cancel leave request
    Given user has leave request with status "<status>"
    When user navigates to My Leave
    And user selects leave request
    And user clicks on cancel button
    And user confirms cancellation
    Then leave should be cancelled successfully
    And leave status should change to "<final_status>"

    Examples:
      | status            | final_status |
      | Pending Approval  | Cancelled    |
      | Scheduled         | Cancelled    |

  Scenario Outline: Approve or reject leave as manager
    Given user is logged in as manager
    And user navigates to Leave module
    And there are pending leave requests from "<employee_name>"
    When user selects leave request
    And user clicks on "<action>" button
    And user enters comment "<comment>"
    Then leave status should change to "<final_status>"
    And employee should receive notification

    Examples:
      | employee_name | action  | comment           | final_status |
      | John Doe      | Approve | Approved for time | Approved     |
      | Jane Smith    | Reject  | Insufficient days | Rejected     |