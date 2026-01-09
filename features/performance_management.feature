Feature: Performance Management

  Background:
    Given user is logged in as admin
    And user navigates to Performance module

  Scenario Outline: Create performance review for employees
    When user clicks on Manage Reviews
    And user clicks on Add button
    And user selects employee "<employee_name>"
    And user selects review period "<review_period>"
    And user selects supervisor "<supervisor_name>"
    And user selects due date "<due_date>"
    And user clicks on save button
    Then performance review should be created successfully
#    And review should appear in reviews list
#    And review status should be "<status>"

    Examples:
      | employee_name       | review_period | supervisor_name    | due_date   | status      |
      | Russel Hamilton     | 2026-Q1       | Sara  Tencrady    | 2026-04-10 | Activated   |
      | Rebecca Harmony     | 2026-Q2       | Sania Shaheen      | 2026-07-10 | Activated   |

#  Scenario: Configure performance review template
#    When user navigates to Configure
#    And user clicks on KPIs
#    And user clicks on Add button
#    And user enters KPI title "Code Quality"
#    And user selects job title "Developer"
#    And user clicks on save button
#    Then KPI should be added successfully