@app2 @regression @TC001
Feature: Google regression
  Scenario: Search Google in regression suite
    Given I open the app2 application
    And I load common data
    And I load all application common data
    And I load common data for app2 application
    And I load app2 test case data "TC001"
    When I search Google for "Playwright Python"
    Then Google returns search results
