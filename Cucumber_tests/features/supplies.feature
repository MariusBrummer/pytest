Feature: Plan a stop

  Scenario: Plan a stop for groceries
    Given I have enough supplies to make 100 tacos
    When 80 tacos are ordered
    Then I will plan a stop for groceries