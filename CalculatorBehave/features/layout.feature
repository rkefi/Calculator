Feature: Layout

  Scenario: Controls Presence
    Given I navigate to the Calculator  page
    When The Calculator main page is displayed
    Then Ten numeric buttons should be visible and enabled
    And Operations buttons should be visible and enabled
    And I see an expression and result display
    And The expression and output fields are empty
