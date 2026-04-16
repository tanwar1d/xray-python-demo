Feature: Login functionality

  Scenario: Successful login
    Given user is on login page
    When user enters valid credentials
    Then login should be successful

  Scenario: Failed login
    Given user is on login page
    When user enters invalid credentials
    Then login should fail