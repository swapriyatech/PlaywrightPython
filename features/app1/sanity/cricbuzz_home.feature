@app1 @sanity @TC001
Feature: Cricbuzz sanity
  Scenario: Open Cricbuzz home page in sanity suite
    Given I open the app1 application
    And I load common data
    And I load app1 test case data "TC001"
    Then the Cricbuzz page has a title
