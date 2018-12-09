Feature: Operations
  
  Scenario Outline: Enter Expression With Single Digit Numbers Without Evaluation
    Given I navigate to the Calculator  page
    And The Calculator main page is displayed
    When I enter a single digit number <single_digit>
    And I choose an arithmetic operation "DIV"
    And I enter a single digit number <second_single_digit>
    Then The output display remains empty
    
    Examples:
      | single_digit | second_single_digit |
      | 1 | 2 |
      | 3 | 4 |
      | 5 | 6 |
      | 7 | 8 |
      | 9 | 0 |
      
  Scenario Outline: Enter Expression With Single Digit Numbers With Evaluation
    Given I navigate to the Calculator  page
    And The Calculator main page is displayed
    When I enter a single digit number <single_digit>
    And I choose an arithmetic operation "PLUS"
    And I enter a single digit number <second_single_digit>
    And I evaluate my expression
    Then The output display is updated with the result of the evaluation of my expression <expected_result>
    
    Examples:
      | single_digit | second_single_digit | expected_result |
      | 1 | 2 | 3 |
      | 3 | 4 | 7 |
      | 5 | 6 | 11 |
      | 7 | 8 | 15 |
      | 9 | 0 | 9 |
      
  Scenario Outline: Enter Expression With Multiple Digits Numbers With Evaluation
    Given I navigate to the Calculator  page
    And The Calculator main page is displayed
    When I enter a multiple digit number <multi_digit>
    And I choose an arithmetic operation "PLUS"
    And I enter a single digit number <single_digit>
    And I choose an arithmetic operation "MULT"
    And I enter a multiple digit number <second_multi_digit>
    And I evaluate my expression
    Then The output display is updated with the result of the evaluation of my expression <expected_result>
    
    Examples:
      | multi_digit | single_digit | second_multi_digit | expected_result |
      | 101 | 2 | 1245 | 2591 |
      | 13 | 4 | 125 | 513 |
      | 15 | 6 | 20 | 135 |
      | 227 | 8 | 315 | 2747 |
      | 129 | 1 | 10 | 139 |
      
  Scenario Outline: Enter Expression With Multiple Digits Numbers And Delete The Last Input
    Given I navigate to the Calculator  page
    And The Calculator main page is displayed
    And I enter a multiple digit number <multi_digit>
    When I press the delete button
    And I evaluate my expression
    Then Only My Last Input Is Deleted <expected_result>
    
    Examples:
      | multi_digit | expected_result |
      | 12345 | 1234 |
      | 543584 | 54358 |
      | 236 | 23 |
      | 12 | 1 |
      | 2000 | 200 |
  
  Scenario: Invalid Expression Error Check
    Given I navigate to the Calculator  page
    And The Calculator main page is displayed
    And I enter a single digit number 2
    And I choose an arithmetic operation "PLUS"
    And I choose an arithmetic operation "MULT"
    When I evaluate my expression
    Then The Output Displays "ERR"
    
  Scenario: Invalid Division Expression Error Check
    Given I navigate to the Calculator  page
    And The Calculator main page is displayed
    And I enter a single digit number 2
    And I choose an arithmetic operation "DIV"
    And I enter a single digit number 0
    When I evaluate my expression
    Then The Output Displays "Infinity"