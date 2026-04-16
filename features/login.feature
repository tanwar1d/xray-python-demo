Feature: Login functionality

  @SAU-22
  Scenario: Successful login
    Given user is on login page
    When user enters valid credentials
    Then login should be successful

  @SAU-23
  Scenario: Failed login
    Given user is on login page
    When user enters invalid credentials
    Then login should fail