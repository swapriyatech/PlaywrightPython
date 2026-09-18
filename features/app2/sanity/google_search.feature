@app2 @sanity
Feature: Google sanity
  Scenario: Search Google in sanity suite
    Given I search Google for "Playwright Python"
    Then Google returns search results
