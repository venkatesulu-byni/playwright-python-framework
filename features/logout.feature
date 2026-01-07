Feature: Logout Functionality

  Background:
    Given user is logged in to OrangeHRM application

  Scenario: Successful logout from application
    When user clicks on user profile dropdown
    And user clicks on logout option
    Then user should be logged out successfully
    And user should be redirected to login page


#  Scenario: Session timeout logout
#    Given user has been inactive for configured timeout period
#    Then user should be automatically logged out
#    And user should see session timeout message
#    And user should be redirected to login page