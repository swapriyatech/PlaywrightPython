@app2 @e2e
Feature: Google end to end
  Scenario: Search Google end to end
    Given I search Google for "Playwright Python"
    Then Google returns search results
