@app1 @regression
Feature: Cricbuzz regression
  Scenario: Open Cricbuzz home page in regression suite
    When I open the Cricbuzz home page
    Then the Cricbuzz page has a title
