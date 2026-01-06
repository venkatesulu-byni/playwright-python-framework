Feature: Login Functionality

  Background:
    Given user navigates to OrangeHRM login page "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

  Scenario: Successful login with valid credentials
    When user enters username "Admin"
    And user enters password "admin123"
    And user clicks on login button
    Then user should be redirected to dashboard page
    And user should see Dashboard

  Scenario Outline: Login with invalid credentials
    When user enters username "<username>"
    And user enters password "<password>"
    And user clicks on login button
    Then user should see error message "<error_message>"
    And user should remain on login page

    Examples:
      | username    | password        | error_message      |
      | InvalidUser | admin123        | Invalid credentials|
      | Admin       | wrongpassword   | Invalid credentials|
      | Admin123    | wrongpass123    | Invalid credentials|
      | TestUser    | test@123        | Invalid credentials|

  Scenario Outline: Login with empty or missing credentials
    When user enters username "<username>"
    And user enters password "<password>"
    And user clicks on login button
    Then user should see validation message "<username_error>" for username field
    And user should see validation message "<password_error>" for password field

    Examples:
      | username | password | username_error | password_error |
      | Empty    | Empty    | Required       | Required       |
      | Admin    | Empty    | NA             | Required       |
      | Empty    | admin123 | Required       | NA             |

  Scenario: Forgot password functionality
    When user clicks on "Forgot your password?" link
    Then user should be redirected to reset password page
    And user should see username field for password reset