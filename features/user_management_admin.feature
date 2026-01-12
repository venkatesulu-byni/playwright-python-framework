Feature: User Management (Admin)

  Background:
    Given user is logged in as admin
    And user navigates to Admin module

  Scenario Outline: Add new system user with different roles
    When user clicks on Add User button
    And user selects user role as "<user_role>"
    And user enters employee name "<employee_name>"
    And user selects status as "<status>"
    And user enters username "<username>"
    And user enters password "<password>"
    And user confirms password "<password>"
    And user clicks on save button
    Then new user should be created successfully
    And user should see success message "Successfully Saved"
    And new user "<username>" should appear in user list

    Examples:
      | user_role | employee_name | status   | username    | password    |
      | Admin     | John Doe      | Enabled  | johndoe123  | Test@1234   |
      | ESS       | Jane Smith    | Enabled  | janesmith1  | Pass@5678   |
      | Supervisor| Robert Wilson | Enabled  | rwilson99   | Admin@999   |
      | ESS       | Sarah Johnson | Disabled | sjohnson22  | User@2468   |

  Scenario Outline: Search users by different criteria
    When user enters username "<username>" in search field
    And user selects user role "<user_role>"
    And user selects status "<status>"
    And user clicks on search button
    Then search results should display matching users
    And results should contain user "<expected_user>"

    Examples:
      | username   | user_role  | status   | expected_user |
      | johndoe123 | Admin      | Enabled  | johndoe123    |
      | janesmith1 | ESS        | Enabled  | janesmith1    |
      |            | Supervisor | Enabled  | rwilson99     |
      | sjohnson22 | ESS        | Disabled | sjohnson22    |

  Scenario: Delete user account
    Given user "testuser123" exists in system
    When user searches for username "testuser123"
    And user selects user checkbox
    And user clicks on delete button
    And user confirms deletion
    Then user should be deleted successfully
    And user "testuser123" should not appear in user list