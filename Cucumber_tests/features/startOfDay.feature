Feature: Start of day

  Scenario: Buy groceries for 100 tacos a the start of the day
    Given It is the start of the day
    When I buy fresh supplies
    Then I have to buy supplies for 100 tacos