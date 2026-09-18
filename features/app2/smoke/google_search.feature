@app2 @smoke @TC001
Feature: Google search
  Scenario: Search for Playwright documentation
    Given I open the app2 application
    And I load common data
    And I load all application common data
    And I load common data for app2 application
    And I load app2 test case data "TC001"
    When I search Google for "Playwright Python"
    Then Google returns search results
