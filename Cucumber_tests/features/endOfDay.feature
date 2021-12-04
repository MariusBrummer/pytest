Feature: End of day
  Description

  Scenario: Don't buy groceries near the end of the working day
    Given It is 3 hours before <the> end of the shift
    When When I have no stock
    Then I won't plan a stop for fresh groceries

Examples:
    | Header 1 | Header 2 | Header 3 |
    | Value 1  | Value 2  | Value 3  |