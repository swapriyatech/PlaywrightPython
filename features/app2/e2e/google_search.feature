@app2 @e2e @TC001
Feature: Google end to end
  Scenario: Search Google end to end
    Given I open the app2 application
    And I load common data
    And I load app2 test case data "TC001"
    When I search Google for "Playwright Python"
    Then Google returns search results
