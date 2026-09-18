@app1 @e2e @TC001
Feature: Cricbuzz end to end
  Scenario: Open Cricbuzz home page end to end
    Given I open the app1 application
    And I load common data
    And I load app1 test case data "TC001"
    Then the Cricbuzz page has a title
