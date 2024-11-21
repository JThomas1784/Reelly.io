# Created by jamontethomas at 11/6/24
Feature: User can click "Connect the company" on the left side of the main page

  Scenario: User clicks "Connect the company" button
    Given I am on the main page
    And I log in with valid credentials
    When I click "Connect the company"
    Then I should see the correct new tab opened