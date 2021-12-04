Feature: Stock left

  Scenario: Stock left at the end of the day
    Given I have stock left
    When It is the end of day
    Then I will take the stock home with me