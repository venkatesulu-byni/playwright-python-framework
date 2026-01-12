Feature: Recruitment Management

  Background:
    Given user is logged in as admin
    And user navigates to Recruitment module

  Scenario Outline: Add different job vacancies
    When user clicks on Vacancies
    And user clicks on Add button
    And user enters vacancy name "<vacancy_name>"
    And user selects job title "<job_title>"
    And user enters number of positions "<positions>"
    And user selects hiring manager "<hiring_manager>"
    And user selects status "<status>"
    And user clicks on save button
    Then vacancy should be created successfully
    And vacancy "<vacancy_name>" should appear in vacancy list

    Examples:
      | vacancy_name           | job_title          | positions | hiring_manager | status |
      | Senior Developer       | Software Engineer  | 2         | John Manager   | Active |
      | QA Engineer            | Quality Assurance  | 1         | Jane Lead      | Active |
      | Business Analyst       | Business Analyst   | 3         | Bob Director   | Active |
      | UI/UX Designer         | Designer           | 1         | Sarah Manager  | Active |

  Scenario Outline: Add candidate application
    Given vacancy "<vacancy_name>" exists
    When user clicks on Candidates
    And user clicks on Add button
    And user enters first name "<first_name>"
    And user enters last name "<last_name>"
    And user enters email "<email>"
    And user selects vacancy "<vacancy_name>"
    And user clicks on save button
    Then candidate should be added successfully
    And candidate status should be "Application Initiated"

    Examples:
      | vacancy_name     | first_name | last_name | email                  |
      | Senior Developer | Michael    | Brown     | mbrown@example.com     |
      | QA Engineer      | Emily      | Davis     | edavis@example.com     |
      | Business Analyst | David      | Martinez  | dmartinez@example.com  |