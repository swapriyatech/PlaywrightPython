@app2 @smoke @sanity @regression
Feature: Google search
  Scenario: Search for Playwright documentation
    Given I search Google for "Playwright Python"
    Then Google returns search results
