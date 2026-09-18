@app1 @e2e
Feature: Cricbuzz end to end
  Scenario: Open Cricbuzz home page end to end
    When I open the Cricbuzz home page
    Then the Cricbuzz page has a title
