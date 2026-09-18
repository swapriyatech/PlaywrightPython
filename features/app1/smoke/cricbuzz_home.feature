@app1 @smoke @TC001
Feature: Cricbuzz home
  Scenario: Open Cricbuzz home page
    Given I launch the browser
    And I open the app1 application
    And I load common data
    And I load all application common data
    And I load common data for app1 application
    And I load app1 test case data "TC001"
    Then the Cricbuzz page has a title
