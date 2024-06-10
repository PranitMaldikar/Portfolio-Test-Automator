# Portfolio-Test-Automator

## Overview

"Portfolio-Test-Automator" is a Selenium-based testing framework using Behave for behavior-driven development. This project focuses on automating functional tests for a web-based trading platform, specifically covering user authentication, stock transactions, and validation of transaction confirmations.

## Setup

1. **Environment Variables**: Define variables like `USER_NAME`, `PASSWORD`, `LOGIN_URL`, etc., in your environment for secure access.
2. **Driver Setup**: Configure the Chrome WebDriver in the global setup to ensure availability for all tests.

## Test Scenarios

- **Login Functionality**: Automate the user login process, ensuring secure access to the platform.
- **Stock Transactions**:
  - **Buying Stocks**: Automate the process of searching for a stock symbol ("AAPL"), selecting an order type, entering the quantity, and confirming the order.
  - **Confirmation Validation**: Assert the presence of a confirmation message post-transaction to verify that the stock order was successfully created.

## Running Tests

Execute the tests using the `behave` command in the terminal, ensuring all dependencies are correctly set up and that the environment is properly configured.

## Error Handling

Incorporate `WebDriverWait` for dynamic content handling, and manage exceptions such as `TimeoutException` to tackle elements not found or interactable within the timeout period.

## Conclusion

The "Portfolio-Test-Automator" project efficiently handles critical functionalities of a trading platform, ensuring that key features like login and stock transactions are functioning as expected through automated tests.
