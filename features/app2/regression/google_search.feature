@app2 @regression
Feature: Google regression
  Scenario: Search Google in regression suite
    Given I search Google for "Playwright Python"
    Then Google returns search results
