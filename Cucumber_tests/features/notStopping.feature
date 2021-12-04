Feature: Not planning a stop for groceries

  Scenario: Not planning a stop
    Given I have enough supplies to make 100 tacos
    When I have less than 80 orders
    Then I will not plan a stop for groceries