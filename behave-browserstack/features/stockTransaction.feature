Feature: Stock Transactions
  As an investor
  I want to perform stock transactions
  So that I can manage my investments effectively

  Scenario: Login
    Given the user has navigated to the login page
    And the user logs in with valid credentials

  Scenario: View dashboard
    Given the user has navigated to the dashboard
    Then the user should see their portfolio 

  Scenario: Buy Stock
    Given the user has a verified payment method
    Then the user searches for a stock inside 'Symbol' field on the dashboard using the ticker symbol "AAPL"
    And the user selects 'Market' in the 'Order Type' dropdown
    And the user enters '2' in the quantity field
    And the user clicks the 'Review Order' button
    And the user clicks the 'Confirm Order' button
    Then the user should receive a confirmation saying 'Order Created'
    

    
    
   